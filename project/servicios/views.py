from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def home(request):
    #Archivo HTML con template
    template = loader.get_template('home.html')
    #Lógica de la vista
    context = {}
    #Respuesta
    return HttpResponse(template.render(context,request))

def sn(request):
    #Archivo HTML con template
    template = loader.get_template('SOBRENOSOTROS.html')
    #Lógica de la vista
    context = {}
    #Respuesta
    return HttpResponse(template.render(context,request))