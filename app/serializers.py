from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Categoria, Enlace

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'titulo',)

class EnlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enlace
        fields = ('url', 'titulo', 'enlace', 'votos', 'usuario', 'categoria', 'timestamp',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email',)
