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

class Mensaje(models.Model):
    
    cuerpo = models.TextField(blank=False, default='')
    remitente = models.ForeignKey(Usuario,related_name='remitente',default='',unique=True)
    destinatario = models.ForeignKey(Usuario,related_name='destinatario',default='',unique=True)
    
    def __str__(self):
        return self.cuerpo
        
class DetalleMensaje(models.Model):
    
    cuerpo = models.TextField(blank=False, default='')
    usuario = models.ForeignKey(Usuario,default='',unique=True)
    fecha = models.DateTimeField(auto_now=True)
    mensaje = models.ForeignKey(Mensaje)
    
    def __str__(self):
        return self.cuerpo

class Imagen(models.Model):
    
    codigo = models.AutoField(primary_key=True)
    link = models.ImageField(upload_to='imagenes')
    descripcion = models.TextField()
    publicacion = models.ForeignKey(Publicacion)
    
    def __str__(self):
        return self.link
    
class Comentario(models.Model):
    
    codigo = models.AutoField(primary_key=True)
    publicacion = models.ForeignKey(Publicacion)
    fecha = models.DateField()
    cuerpo = models.TextField(blank=True, default='')
    autor = models.ForeignKey(Usuario)
    
    def __str__(self):
        return self.cuerpo
