from dataclasses import field
from unicodedata import name
from django.forms import ModelForm
from .models import *

class RevForm(ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'
    
