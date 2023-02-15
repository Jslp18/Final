from django import forms
from .models import Servicio

#Crear formulario
class ServicioForm(forms.ModelForm):

    #Metaclase
    class Meta:
        model = Servicio

        #especificar los campos
        fields = [
            'imagen',
            'titulo',
            'descripcion',
            'precio'
        ]
