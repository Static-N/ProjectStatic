from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.core.paginator import Paginator
from .forms import RevForm
from .filters import displayCard

# Create your views here.

from django.template import Context, loader

def g_cat(pk):
    if pk == 'Anime':
        return 1
    elif pk == 'Web Series':
        return 2
    elif pk == 'Drama':
        return 3
    elif pk == 'Movie':
        return 4

def home(request):
    return render(request,'app/home.html')


def WSmain(request,pk):
    l = g_cat(pk)
    Cards = mainInfo.objects.filter(catgrys = l)
    f1 = Cards.first()
    f = f1.catgrys.all()
    fn = f.first()
    gen = genere.objects.all()
    filCar = displayCard(request.GET, queryset=Cards)
    Cards = filCar.qs
    context = {'Cards':Cards,'fn':fn , 'filCar':filCar,'gen':gen}
    return render(request,'app/webSeries.html',context)

def WSinfo(request,pk):
    content = mainInfo.objects.get(name = pk)
    f = content.catgrys.all()
    fn = f.first()
    r = Paginator(content.reviews_set.all(),5)
    page = request.GET.get('page')
    rev = r.get_page(page)
    filCar = displayCard()
    form = RevForm(initial={'name':content.id})
    if request.method == 'POST':
        form = RevForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    context = {'content':content, 'rev':rev,'fn':fn ,'form':form,'filCar':filCar}
    return render(request,'app/WSinfo.html',context)

def gen(request):
    Cards = mainInfo.objects.all()
    filCar = displayCard(request.GET, queryset=Cards)
    gen = genere.objects.all()
    cat = Catgry.objects.all()
    Cards = filCar.qs
    con = {'Cards':Cards,'gen':gen,'filCar':filCar,'cat':cat}
    return render(request,'app/general.html',con)