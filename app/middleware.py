from django.shortcuts import redirect
from random import choice

def de_donde_vengo():
    paises = ['Colombia', 'Mexico', 'Argentina', 'Peru']
    return choice(paises)

class PaisMiddleware():
    pass
