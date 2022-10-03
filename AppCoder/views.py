from tkinter import N
from django.http import HttpResponse

from django.shortcuts import render

#from django.template import loader


# Create your views here.

from AppCoder.models import Familia

def crear_familia(request):
    
    familiar_1 = Familia (nombre="Ricardo" , apellido="Medina" , correo="mini@gmail.com", edad="55", fecha_de_nacimiento="1966-7-31")
    familiar_2 = Familia (nombre="Leandro" , apellido="Medina" , correo="lean@hotmail.com.ar", edad="32", fecha_de_nacimiento="1990-5-15")
    familiar_3 = Familia (nombre="Mariano" , apellido="Gonsalo" , correo="mari12@yahoo.com", edad="17", fecha_de_nacimiento="2003-10-1")
    
    return HttpResponse()
    
    