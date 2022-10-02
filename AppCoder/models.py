import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familia (models.Model):
    
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    correo = models.EmailField()
    edad = models.CharField(max_length=3)
    fecha_de_nacimiento = models.DateField()