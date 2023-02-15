from django.db import models
from django import forms

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
