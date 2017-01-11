from django.shortcuts import redirect
from random import choice

def de_donde_vengo():
    paises = ['Colombia', 'Mexico', 'Argentina', 'Peru']
    return choice(paises)

class PaisMiddleware:
    def process_request(self, request):
        pais = de_donde_vengo()
        if pais == 'Mexico':
            return redirect('https://google.com')
