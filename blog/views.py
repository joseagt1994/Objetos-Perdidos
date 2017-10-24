from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template import RequestContext
from .models import Publicacion, Imagen, Comentario, Mensaje
from django.contrib.auth.models import User
from .forms import formComentario, formPublicacion, formImagen
import time, requests, json, urllib2
from ipware.ip import get_ip

# Create your views here.

def publicar(request):
    if request.method == 'POST':
        formulario = formPublicacion(request.POST)
        usuario = User.objects.get_by_natural_key('jose')
        if formulario.is_valid():
            pub = formulario.save(commit=False)
            pub.fecha = time.strftime("20%y-%m-%d")
            pub.autor = usuario
            pub.estado = False
            print('Esta es la ip...')
            ip = get_ip(request)
            f = urllib2.urlopen('http://freegeoip.net/json/'+ip)
            json_string = f.read()
            f.close()
            location = json.loads(json_string)
            print(location)
            lo = location['longitude']
            la = location['latitude']
            print(lo)
            print(la)
            pub.longitud = lo
            pub.latitud = la
            pub.titulo = request.POST['titulo']
            pub.descripcion = request.POST['descripcion']
    	    pub.save()
    	    print(pub.codigo)
    	    return HttpResponseRedirect('agregarImagenes/'+str(pub.codigo))
    formulario = formPublicacion()
    formImagenes = formImagen()
    return render_to_response('publicar.html',{'formulario':formulario,'formImg':formImagenes}, context_instance= RequestContext(request))

def enviarMensaje(request,cod_publicacion):
    pub = Publicacion.objects.get(codigo=cod_publicacion)
    autor = pub.autor
    return render_to_response('reclamar.html',{'autor':autor},context_instance=RequestContext(request))

def agregarImagenes(request,cod_publicacion):
    pub = Publicacion.objects.get(codigo=cod_publicacion)
    
    if request.method == 'POST':
        print('HOLA!')
        formulario = formImagen(request.POST,request.FILES)
        print('Es:...')
        print(formulario.is_valid())
        if formulario.is_valid():
            print('Funciona!')
            imagen = formulario.save(commit=False)
            print('Link....')
            imagen.ruta = request.FILES['link']
            imagen.publicacion = pub
            imagen.save()
    formulario = formImagen()
    imagenes = Imagen.objects.raw('SELECT * FROM blog_imagen WHERE publicacion_id = %s',[cod_publicacion])
    print('Imagenes...')
    print(imagenes)
    return render_to_response('imagenes.html',{'formulario':formulario,'imagenes':imagenes},context_instance=RequestContext(request))

def verPublicacion(request):
    imagenes = Imagen.objects.raw('SELECT * FROM blog_imagen GROUP BY publicacion_id')
    return render_to_response('visualizar.html',{'imagenes':imagenes},context_instance=RequestContext(request))
    #return render(request, 'visualizar.html', {'publicaciones':publicaciones})
    
def perfil(request,cod_user):
     #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    usuario = getUsuario(cod_user)
    mensajes = cantidad_bandejaEntrada(cod_user)
   # publicaciones = Publicacion.objects.get(autor=usuario)
    
    
    return render_to_response("perfil.html",{'mensajes':mensajes},context_instance= RequestContext(request))

def vistaLogin(request):
    request.session['login'] = None   
    if request.method =='POST':
        usuario = request.POST['txtUsuario']
        contra = request.POST['txtPass']
        existe = Usuario.objects.get(password = contra,nombre=usuario)
       
        if(existe !=None):
            request.session['login'] = usuario
            print request.session['login']
            return HttpResponseRedirect('perfil/'+str(existe.codigo))

    return render_to_response("login.html",context_instance= RequestContext(request))
