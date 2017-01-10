# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from .models import Categoria, Enlace

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by('-votos').all()
    return render_to_response('index.html', { 'categorias': categorias, 'enlaces': enlaces })

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    enlaces = Enlace.objects.order_by('-votos').filter(categoria=categoria)
    return render_to_response('index.html', { 'categorias': categorias, 'enlaces': enlaces })

def plus(request, enlace_id):
    enlace = Enlace.objects.get(pk=enlace_id)
    enlace.votos = enlace.votos + 1
    enlace.save()
    return HttpResponseRedirect('/')

def minus(request, enlace_id):
    enlace = Enlace.objects.get(pk=enlace_id)
    enlace.votos = enlace.votos - 1
    enlace.save()
    return HttpResponseRedirect('/')
