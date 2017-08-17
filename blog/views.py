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
    
