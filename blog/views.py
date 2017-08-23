from django.shortcuts import render

# Create your views here.

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
