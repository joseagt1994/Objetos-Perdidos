from django import forms
from .models import Publicacion,Comentario,Mensaje,Imagen

class formPublicacion(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = []
