from django.urls import path
from . import views

urlpatterns = [
    path('empleados/pagina-empleados', views.func_empleados)
]