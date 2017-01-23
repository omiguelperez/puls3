from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Categoria, Enlace

# Create your tests here.

class EnlaceTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(titulo='Categoria de prueba')
        self.usuario = User.objects.create_user(username='miusuario', password='claveusuario')

    def test_es_popular(self):
        enlace = Enlace.objects.create(titulo='Enlace de prueba',
            enlace='http://google.com', categoria=self.categoria, usuario=self.usuario)

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

    def test_views(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('enlaces'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

        self.client.login(username='miusuario', password='claveusuario')
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        self.client.login(username='miusuario', password='claveusuario')

        data = {}
        data['titulo'] = 'Titulo del enlace'
        data['enlace'] = 'https://google.com/'
        data['categoria'] = self.categoria.id

        response = self.client.post(reverse('add'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Enlace.objects.count(), 1)

        enlace = Enlace.objects.all()[0]
        self.assertEqual(enlace.titulo, data['titulo'])
        self.assertEqual(enlace.enlace, data['enlace'])
        self.assertEqual(enlace.categoria, self.categoria)
