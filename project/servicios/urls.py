from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    #ruta, vista, nombre interno
    path('Home', views.home, name='home'),
    path('SobreNosotros', views.sn, name='sn'),
    path('Login', views.login, name='login'),

    path('Servicios', views.listarServicios, name='servicios'),
    path('Servicios/AgregarServicio', views.crear_servicio, name='nuevo_servicio'),
    path('Servicios/<id>', views.servicio_view, name='info_servicio'),
    path('Servicios/ActualizarServicio/<id>', views.update_servicio, name='actualizar_servicio'),
    path('Servicios/EliminarServicio/<id>', views.delete_view, name='eliminar_servicio'),
]