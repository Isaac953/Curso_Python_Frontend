from django.urls import path
from . import views

urlpatterns = [
    path('lista-usuarios', views.func_index),
]