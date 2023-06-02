from django.urls import path
from . import views

urlpatterns = [
    path('persona', views.func_index),
    path('persona/<nombre>/<int:edad>', views.mostrar_nombre_edad),
]