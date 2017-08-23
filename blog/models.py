from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Imagen(models.Model):
    
    codigo = models.AutoField(primary_key=True)
    link = models.ImageField(upload_to='imagenes')
    descripcion = models.TextField()
    publicacion = models.ForeignKey(Publicacion)
    
    def __str__(self):
        return self.link
