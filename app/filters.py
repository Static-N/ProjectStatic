from dataclasses import fields
from unicodedata import name
import django_filters
from .models import *
from django_filters import CharFilter

class displayCard(django_filters.FilterSet):
    name = CharFilter(field_name='name',lookup_expr='icontains')
    class Meta:
        model = mainInfo
        fields = ('name','generes','catgrys')
