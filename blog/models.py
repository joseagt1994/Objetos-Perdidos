from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publicacion(models.Model):
    
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    fecha = models.DateField()
    longitud = models.FloatField()
    latitud = models.FloatField()
    descripcion = models.TextField(blank=False, default='')
    estado = models.BooleanField()
    autor = models.ForeignKey(User)
    
    def __str__(self):
        return self.titulo
      
class Imagen(models.Model):
    
    codigo = models.AutoField(primary_key=True)
    link = models.ImageField(upload_to='imagenes')
    descripcion = models.TextField()
    publicacion = models.ForeignKey(Publicacion)
    
    def __str__(self):
        return self.link
