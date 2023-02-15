from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
#Importar modelo para CRUD y formulario
from .models import Servicio
from .forms import ServicioForm

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

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                auth_login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'Usuario no válido')
        else:
            messages.error(request, 'Verifique los datos de inicio de sesión')
            
    form=AuthenticationForm()
    return render(request, '../templates/registration/login.html', {'form':form})

#Vista para listar servicios
def listarServicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios':servicios}
    template = loader.get_template('servicios/servicios.html')
    return HttpResponse(template.render(context, request))

#Vista para detalles de un servicio
def servicio_view(request, id):
    context = {}
    context['object'] = Servicio.objects.get(id = id)
    return render(request, 'servicios/servicio_detalle.html', context)

#Vista para crear un servicio
def crear_servicio(request):
    context={}
    form = ServicioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('servicios')
    context['form'] = form
    return render(request, 'servicios/crear_servicio.html', context)

#Vista para actualizar un servicio
def update_servicio(request, id):
    context = {}
    context['object'] = Servicio.objects.get(id = id)
    obj = get_object_or_404(Servicio, id = id)
    #formulario que contiene la instancia
    form = ServicioForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('servicios')
    context['form'] = form
    return render(request, 'servicios/actualizar_servicio.html', context)

#Vista para eliminar un servicio
def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Servicio, id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('servicios')
    return render(request, 'servicios/eliminar_servicio.html', context)