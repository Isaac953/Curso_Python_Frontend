from django.urls import path
from . import views

app_name = 'empleados_app'

urlpatterns = [
    path(
    'empleados/listar-empleados', 
    views.listar_empleados,
    name='listar-empleados'),
    path(
    'empleados/crear-empleado', 
    views.CrearEmpleado.as_view(),
    name='crear-empleado'),
]