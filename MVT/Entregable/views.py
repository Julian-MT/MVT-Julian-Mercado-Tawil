from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from Entregable.models import  Familiar
from datetime import datetime
# Create your views here.

def inicio(request):
    plantilla=loader.get_template('inicio.html')
    documento=plantilla.render()
    return HttpResponse(documento)

def familiares(request):
    
    Papa=Familiar(nombre='Daniel', edad=62, fecha= datetime(1960,3,16))
    Mama=Familiar(nombre='Silvia', edad=56, fecha=datetime(1965,8,24))
    Hermano=Familiar(nombre='Juan', edad=25, fecha=datetime(1996,6,2))

    Papa.save()
    Mama.save()
    Hermano.save()

    plantilla=loader.get_template('familiares.html')
    documento=plantilla.render({'nombrepa':Papa.nombre, 'edadpa':Papa.edad, 'fechapa':Papa.fecha, 'nombrema':Mama.nombre, 'edadma':Mama.edad, 'fechama':Mama.fecha, 'nombrehe':Hermano.nombre, 'edadhe':Hermano.edad, 'fechahe':Hermano.fecha})
    return HttpResponse(documento)