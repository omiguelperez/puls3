# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template.context import Context
from .models import Categoria, Enlace

def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.all()
    template = get_template('index.html')
    context = Context({ "categorias": categorias, "enlaces": enlaces })
    html = template.render(context)
    return HttpResponse(html)
