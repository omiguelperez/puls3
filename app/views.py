# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic import DetailView, ListView
from .forms import EnlaceForm
from .models import Categoria, Enlace

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by('-votos').all()
    return render(request, 'index.html', { 'request': request, 'categorias': categorias, 'enlaces': enlaces })

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
    return render(request, 'form.html', { 'form': form, 'categorias': categorias })

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    enlaces = Enlace.objects.order_by('-votos').filter(categoria=categoria)
    return render(request, 'index.html', { 'request': request, 'categorias': categorias, 'enlaces': enlaces })

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

class EnlaceListView(ListView):
    model = Enlace
    context_object_name = 'enlaces'
    template_name = 'index.html'

class EnlaceDetailView(DetailView):
    model = Enlace
    template_name = 'index.html'
