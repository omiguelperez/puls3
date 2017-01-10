# Create your views here.

from django.shortcuts import render_to_response
from .models import Categoria, Enlace

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.all()
    return render_to_response('index.html', { "categorias": categorias, "enlaces": enlaces })
