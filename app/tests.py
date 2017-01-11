"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.contrib.auth.models import User
from django.test import TestCase
from .models import Categoria, Enlace

class EnlaceTest(TestCase):
    def test_es_popular(self):
        categoria = Categoria.objects.create(titulo='Categoria de prueba')
        usuario = User.objects.create_user(username='miusuario', password='claveusuario')
        enlace = Enlace.objects.create(titulo='Enlace de prueba',
            enlace='http://google.com', categoria=categoria, usuario=usuario)

        # Probar que el enlace no es popular
        self.assertEqual(enlace.votos, 0)
        self.assertEqual(enlace.es_popular(), False)
        self.assertFalse(enlace.es_popular())

        # Probar que el enlace es popular
        enlace.votos = 20
        enlace.save()
        self.assertEqual(enlace.votos, 20)
        self.assertEqual(enlace.es_popular(), True)
        self.assertTrue(enlace.es_popular())
