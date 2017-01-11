from django.core.urlresolvers import reverse
from random import choice

def frases(request):
    mis_frases = [
        'La vengaza es lucrativa',
        'Sin sacrificio no hay victoria',
        'Un buen acto de vengaza merece otro'
    ]
    return { 'frase': choice(mis_frases) }

def menu(request):
    items = { 'menu': [
        { 'url': reverse('home'), 'name': 'Home' },
        { 'url': reverse('add'), 'name': 'Agregar' }
    ] }
    for item in items['menu']:
        if request.path == item['url']:
            item['active'] = True
    return items
