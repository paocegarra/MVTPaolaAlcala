from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from django.template import loader


# Create your views here.

from AppCoder.models import Familia

def crear_familia(request):
    
    template = loader.get_template("template1.html")
    
    familiar_1 = Familia (nombre="Ricardo" , apellido="Medina" , correo="mini@gmail.com", edad="55", fecha_de_nacimiento="1966-7-31")
    familiar_2 = Familia (nombre="Edudado" , apellido="Luis" , correo="luigii@gmail.com", edad="70", fecha_de_nacimiento="1955-7-31")
    familiar_3 = Familia (nombre="María" , apellido="Lina" , correo="Linida@gmail.com", edad="7", fecha_de_nacimiento="2015-7-31")
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    
    dict_de_contexto = {
         
        "familiar_1" : familiar_1, 
        "familiar_2" : familiar_2,
        "familiar_3" : familiar_3,
        
    }

    res = template.render(dict_de_contexto)
    
    return HttpResponse(res)
    
    