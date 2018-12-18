from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

from .models import Wpis
# Create your views here.

def index(request):
    wpisy = Wpis.objects.all()
    
    wynik=""
    
    for w in wpisy:
        wynik+= f"<ul>{w.tytul}<br>"
    return HttpResponse(wynik)

def index_temp(request):
    
    t = Template('chleb kosztuje {{ chleb }}')
    c = Context({'chleb':'1.90'})
    wynik = t.render(c)
    return HttpResponse(wynik)