from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def familia (request):
    
    familiar1=Familiares(apodo="Susi", edad=47, cumpleanos=("1975-7-12"))
    
    familiar2=Familiares(apodo="Chan", edad=30, cumpleanos="1992-9-20")
    
    familiar3=Familiares(apodo="Flaco", edad=27, cumpleanos="1995-5-25")
    
    familiar1.save()
    familiar2.save()
    familiar3.save()
    
    template=loader.get_template("familia1.html")
    
    context= {"familia1": [familiar1,familiar2,familiar3]}
    
    document=template.render(context)
    return HttpResponse(document)