from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6,decimal_places=2)