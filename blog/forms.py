from django import forms
from .models import Publicacion,Comentario,Mensaje,Imagen

class formPublicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = []
        
class formComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpo']
        
class formImagen(forms.ModelForm):
    class Meta:
        model = Imagen
        fields = ['descripcion','link']
        
class formMensaje(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['cuerpo']

        
