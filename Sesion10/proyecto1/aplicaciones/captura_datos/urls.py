from django.urls import path
from . import views

urlpatterns = [
    path('captura_datos', views.func_index),
    path('captura_datos/result', views.result_data),
]