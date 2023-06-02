from django.urls import path
from . import views

urlpatterns = [
    path('consumo_api', views.func_index),
]