from django import forms
from .models import Enlace

# Create your forms here.

class EnlaceForm(forms.ModelForm):
    class Meta:
        model = Enlace
        exclude = ['votos']
