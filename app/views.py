# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse('Pantalla de inicio')

def post(request, post_id):
    if int(post_id) > 10:
        return HttpResponse('Este post es mayor que 10')
    else:
        return HttpResponse('Este post es menor o igual que 10')


def live(request, live_id, curso_id):
    return HttpResponse('Este es el live %s del curso %s' % (live_id, curso_id))
