# Create your views here.

from django.shortcuts import render_to_response
from datetime import datetime

def hora_actual(request):
    now = datetime.now()
    return render_to_response('hora.html', { 'user': 'omiguelperez', 'now': now })
