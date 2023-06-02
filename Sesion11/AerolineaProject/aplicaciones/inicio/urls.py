from django.urls import path
from . import views

urlpatterns = [
    path('inicio/pagina-inicial', views.func_index),
    path('inicio/listar-personas', views.listar_personas),
    path('inicio/listar-edad', views.listar_edad)
]