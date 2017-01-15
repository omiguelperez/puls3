from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Categoria, Enlace

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('titulo',)

class EnlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enlace
        fields = ('url', 'titulo', 'enlace', 'categoria', 'votos', 'usuario', 'timestamp',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email',)
