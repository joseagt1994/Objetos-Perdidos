from django.contrib import admin
from .models import Publicacion,Imagen,Comentario,Mensaje,Usuario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ['codigo','titulo','fecha','cuerpo','autor']
    
admin.site.register(Imagen)
admin.site.register(Comentario)
admin.site.register(Mensaje)
