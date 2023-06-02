from django.shortcuts import render
import requests

# Create your views here.
def func_index(request):
    url_api = 'https://jsonplaceholder.typicode.com/users'
    datos = requests.get(url_api)
    consumo_api = {
        'titulo': 'Consumo de API',
        'usuarios': datos.json,
    }
    return render(request, 'consumo_api/tarea_api.html', consumo_api)