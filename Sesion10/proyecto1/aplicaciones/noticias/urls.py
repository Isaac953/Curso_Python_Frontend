from django.urls import path
from . import views

urlpatterns = [
    path('noticias', views.func_index),
    path('noticias/resultados', views.search_new),
]