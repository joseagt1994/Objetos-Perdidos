from django.shortcuts import render

# Create your views here.

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
