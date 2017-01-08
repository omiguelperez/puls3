# Create your views here.

from django.http import HttpResponse
import json
import urllib2

def home(request):
    try:
        f = urllib2.urlopen('http://congresorest.appspot.com/diputado/1')
        result = f.read()
    except Exception, e:
        return HttpResponse(e.message)
    diputado = json.loads(result)
    return HttpResponse(diputado['entidad'])

def post(request, post_id):
    if int(post_id) > 10:
        return HttpResponse('Este post es mayor que 10')
    else:
        return HttpResponse('Este post es menor o igual que 10')

def live(request, live_id, curso_id):
    return HttpResponse('Este es el live %s del curso %s' % (live_id, curso_id))
