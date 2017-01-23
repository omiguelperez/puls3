from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .forms import EnlaceForm
from .models import Categoria, Enlace

# Create your views here.

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by('-votos').all()
    return render(request, 'index.html', { 'categorias': categorias, 'enlaces': enlaces })

@login_required
def plus(request, enlace_id):
    enlace = Enlace.objects.get(pk=enlace_id)
    enlace.votos = enlace.votos + 1
    enlace.save()
    return HttpResponseRedirect('/')

@login_required
def minus(request, enlace_id):
    enlace = Enlace.objects.get(pk=enlace_id)
    enlace.votos = enlace.votos - 1
    enlace.save()
    return HttpResponseRedirect('/')

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    enlaces = Enlace.objects.order_by('-votos').filter(categoria=categoria)
    return render(request, 'index.html', { 'categorias': categorias, 'enlaces': enlaces })

@login_required
def add(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form = EnlaceForm(request.POST)
        if form.is_valid():
            enlace = form.save(commit=False)
            enlace.usuario = request.user
            enlace.save()
            return HttpResponseRedirect('/')
    else:
        form = EnlaceForm()
    return render(request, 'form.html', { 'categorias': categorias, 'form': form })

class EnlaceListView(ListView):
    model = Enlace
    template_name = 'index.html'
    context_object_name = 'enlaces'

class EnlaceDetailView(DetailView):
    model = Enlace
    template_name = 'index.html'

from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import CategoriaSerializer, EnlaceSerializer, UserSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class EnlaceViewSet(viewsets.ModelViewSet):
    queryset = Enlace.objects.all()
    serializer_class = EnlaceSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
