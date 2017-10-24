from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template import RequestContext
from objetos.models import Publicacion, Imagen, Comentario, Mensaje, Usuario, DetalleMensaje
from objetos.forms import formComentario, formPublicacion, formImagen, formChat
import time, requests

# Create your views here.
def publicar(request):
    
     #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    
    if request.method == 'POST':
        formulario = formPublicacion(request.POST)
        usuario = Usuario.objects.get(codigo=1)
        if formulario.is_valid():
            pub = formulario.save(commit=False)
            pub.fecha = time.strftime("20%y-%m-%d")
            pub.autor = usuario
            pub.estado = False
            pub.titulo = request.POST['titulo']
            pub.ubicacion = request.POST['ubicacion']
            pub.descripcion = request.POST['descripcion']
    	    pub.save()
    	    print(pub.codigo)
    	    return HttpResponseRedirect('agregarImagenes/'+str(pub.codigo))
    formulario = formPublicacion()
    formImagenes = formImagen()
    return render_to_response('publicar.html',{'formulario':formulario,'formImg':formImagenes}, context_instance= RequestContext(request))

def publicacion_detallada(request,cod_publicacion):
     #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    usuario = Usuario.objects.get(codigo = 1)
    print(usuario.codigo)
    publicacion = Publicacion.objects.get(codigo = cod_publicacion)
    imagenes = Imagen.objects.raw('SELECT * FROM objetos_imagen WHERE publicacion_id = %s',[cod_publicacion])
    print(imagenes)
    return render_to_response('publicacion.html',{'pub':publicacion,'imgs':imagenes},context_instance=RequestContext(request))

def enviarMensaje(request,cod_publicacion):
    #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
         return render(request,"login.html")
    usuario = Usuario.objects.get(codigo=2)
    pub = Publicacion.objects.get(codigo=cod_publicacion)
    autor = pub.autor
    if request.method == 'POST':
        mensaje = Mensaje()
        mensaje.cuerpo = request.POST['descripcion']
        mensaje.remitente = usuario
        mensaje.destinatario = autor
        mensaje.save()
        return HttpResponseRedirect('/visualizar')
    return render_to_response('reclamar.html',{'autor':autor},context_instance=RequestContext(request))

def cantidad_bandejaEntrada(cod_usuario):
    mensajes = Mensaje.objects.raw('SELECT * FROM objetos_mensaje WHERE destinatario_id = %s',[cod_usuario])
    return mensajes

def agregarImagenes(request,cod_publicacion):
    
     #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    
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
    imagenes = Imagen.objects.raw('SELECT * FROM objetos_imagen WHERE publicacion_id = %s',[cod_publicacion])
    print('Imagenes...')
    print(imagenes)
    return render_to_response('imagenes.html',{'formulario':formulario,'imagenes':imagenes},context_instance=RequestContext(request))
    
def reclamar(cod_publicacion):
    publicacion = Publicacion.objects.get(codigo=cod_publicacion)
    if(publicacion != None):
        publicacion.estado = True
        publicacion.save()
        return True
    else:
        print('Publicacion no existe!')
        return False

def getUsuario_codigo(cod_usuario):
    usuario = Usuario.objects.filter(codigo=cod_usuario).first()
    if usuario != None:
        return True
    else:
        return False
        
def getPublicaciones():
    publicaciones = Publicacion.objects.raw('SELECT * FROM objetos_imagen GROUP BY publicacion_id')
    print(len(list(publicaciones)))
    print('Tager se quedo sin bateria jajaja')
    return 1

def reclamar(cod_publicacion):
    publicacion = Publicacion.objects.get(codigo=cod_publicacion)
    if(publicacion != None):
        publicacion.estado = True
        publicacion.save()
        return True
    else:
        print('Publicacion no existe!')
        return False

def verPublicacion(request):
     #agregacion de la validacion del login
    print(request.session['login'])
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    imagenes = Imagen.objects.raw('SELECT * FROM objetos_imagen GROUP BY publicacion_id')
    return render_to_response('visualizar.html',{'imagenes':imagenes},context_instance=RequestContext(request))

def publicacion_detallada(request,cod_publicacion):
     #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    usuario = Usuario.objects.get(codigo = 1)
    print(usuario.codigo)
    publicacion = Publicacion.objects.get(codigo = cod_publicacion)
    imagenes = Imagen.objects.raw('SELECT * FROM objetos_imagen WHERE publicacion_id = %s',[cod_publicacion])
    print(imagenes)
    return render_to_response('publicacion.html',{'pub':publicacion,'imgs':imagenes},context_instance=RequestContext(request))


def cantidad_bandejaEntrada(cod_usuario):
    mensajes = Mensaje.objects.raw('SELECT * FROM objetos_mensaje WHERE destinatario_id = %s',[cod_usuario])
    return mensajes

def enviarMensaje(request,cod_publicacion):
    #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
         return render(request,"login.html")
    usuario = Usuario.objects.get(codigo=2)
    pub = Publicacion.objects.get(codigo=cod_publicacion)
    autor = pub.autor
    if request.method == 'POST':
        mensaje = Mensaje()
        mensaje.cuerpo = request.POST['descripcion']
        mensaje.remitente = usuario
        mensaje.destinatario = autor
        mensaje.save()
        return HttpResponseRedirect('/visualizar')
    return render_to_response('reclamar.html',{'autor':autor},context_instance=RequestContext(request))

def publicarEncontrado(request):
    #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    
    if request.method == 'POST':
        formulario = formPublicacion(request.POST)
        usuario = Usuario.objects.get_by_natural_key('jose')
        if formulario.is_valid():
            pub = formulario.save(commit=False)
            pub.fecha = time.strftime("20%y-%m-%d")
            pub.autor = usuario
            pub.estado = False
            pub.ubicacion = request.POST['ubicacion']
            pub.titulo = request.POST['titulo']
            pub.descripcion = request.POST['descripcion']
    	    pub.save()
    	    print(pub.codigo)
    	    return HttpResponseRedirect('agregarImagenes/'+str(pub.codigo))
    formulario = formPublicacion()
    formImagenes = formImagen()
    return render_to_response('publicar_encontrado.html',{'formulario':formulario,'formImg':formImagenes}, context_instance= RequestContext(request))
    
    
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

def logout(request):
    try:
        request.session['login'] =None
    except:
        HttpResponseRedirect('/')
    return render_to_response("login.html",context_instance= RequestContext(request))    

def registro(request):
    if request.method == 'POST':
        usuario = request.POST['txtUsuario']
        contra = request.POST['txtPass']
        
        try:
            existe = Usuario.objects.get(nombre=usuario)
        except Usuario.DoesNotExist:
            existe = None
            Usuario.objects.create(nombre=usuario,password=contra)
            existe = Usuario.objects.get(nombre=usuario)
            return HttpResponseRedirect('/')
    
    return render_to_response("registro.html",context_instance= RequestContext(request))

def perfil(request,cod_user):
     #agregacion de la validacion del login
    log = request.session['login'] 
    if log ==None:
        return render(request,"login.html")
    usuario = getUsuario(cod_user)
    mensajes = cantidad_bandejaEntrada(cod_user)
    publicaciones = Publicacion.objects.raw('SELECT * FROM objetos_publicacion WHERE autor_id = %s',[cod_user])
    
    return render_to_response("perfil.html",{'mensajes':mensajes},context_instance= RequestContext(request))

def getUsuario_codigo(cod_usuario):
    usuario = Usuario.objects.filter(codigo=cod_usuario).first()
    if usuario != None:
        return True
    else:
        return False
        
def getPublicaciones():
    publicaciones = Publicacion.objects.raw('SELECT * FROM objetos_imagen GROUP BY publicacion_id')
    print(len(list(publicaciones)))
    print('Tager se quedo sin bateria jajaja')
    return 1
  
def conversacion(request,cod_mensaje):
    msj = Mensaje.objects.get(codigo = cod_mensaje)
    chats = DetalleMensaje.objects.get(mensaje = msj)
    
    if request.method == 'POST':
        formulario = formChat(request.POST)
        if formulario.is_valid():
            detalle = formulario.save(commit=False)
            user = Usuario.objects.get(nombre = request.session['login'])
            detalle.usuario = user
            detalle.mensaje = msj
            detalle.save()
            chats = DetalleMensaje.objects.get(mensaje = msj)
    
    return render_to_response("conversacion.html",{'mensaje':msj,'chats':chats},context_instance= RequestContext(request))

def getUsuario(codigo_user):
    usuario = Usuario.objects.get(codigo=codigo_user)
    return usuario
