from django.urls import path
from . import views

urlpatterns = [
    path('calculadora', views.func_index),
    path('calculadora/math', views.math),
]