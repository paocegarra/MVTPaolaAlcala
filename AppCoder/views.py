from tkinter import N
from django.http import HttpResponse

from django.shortcuts import render

#from django.template import loader


# Create your views here.

from AppCoder.models import Familia

def crear_familia(request):
    
    familiar_1 = Familia (nombre="Ricardo" , apellido="Medina" , correo="mini@gmail.com", edad="55")
    
    familiar_1.save()
    
    return HttpResponse(f"Mi papa es: {familiar_1.nombre} {familiar_1.apellido} . Su correo es: {familiar_1.correo} . Su edad es: {familiar_1.edad}  ")
    
    