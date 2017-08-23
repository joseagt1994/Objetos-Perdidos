from django.test import TestCase
from django.test.client import Client
from .views import reclamar
from .models import Publicacion

# Create your tests here.

class ReclamoTestCase(TestCase):
    def setUp(self):
        self.c = Client()
    
    def test_reclamar(self):
        cod_publicacion = 37
        self.assertEqual(reclamar(cod_publicacion),True)
        
class BlogTestCase(TestCase):
    def setUp(self):
        self.c = Client()
        
    def test_visualizar(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_publicar(self):
        response = self.c.get('/visualizar')
        self.assertEqual(response.status_code, 200)
        
    def test_publicar_encontrado(self):
        response = self.c.get('/encontrado')
        self.assertEqual(response.status_code, 200)
