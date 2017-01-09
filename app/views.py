# Create your views here.

from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from datetime import datetime

def hora_actual(request):
    now = datetime.now()
    template = get_template('hora.html')
    context = Context({ "now": now })
    html = template.render(context)
    return HttpResponse(html)
