from django.contrib import admin

from app.forms import RevForm

# Register your models here.
from .models import *
admin.site.register(genere)
admin.site.register(mainInfo)
admin.site.register(Reviews)
admin.site.register(Catgry)