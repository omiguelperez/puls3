from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=140)

    def __unicode__(self):
        return self.titulo

class Enlace(models.Model):
    titulo = models.CharField(max_length=140)
    enlace = models.URLField()
    votos = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria)
    usuario = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s - %s' % (self.titulo, self.enlace)

    def mis_votos_en_imagen_rosada(self):
        return 'http://placehold.it/250x150/E8117F/FFFFFF?text=%s+votos' % self.votos

    def es_popular(self):
        return self.votos > 10
    es_popular.boolean = True

class Agregador(models.Model):
    titulo = models.CharField(max_length=140)
    enlaces = models.ManyToManyField(Enlace)

    class Meta:
        verbose_name_plural = 'Agregadores'

    def __unicode__(self):
        return self.titulo
