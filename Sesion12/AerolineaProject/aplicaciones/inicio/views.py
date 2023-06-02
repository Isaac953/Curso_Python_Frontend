from django.shortcuts import render
# Create your views here.
def func_index(request):
    return render(request, 'inicio/index.html')

def listar_personas(request):
    personas = {
        'titulo': 'Lista de Personas',
        'nombres': ['alicia', 'beto', 'camila', 'diana']
    }
    return render(request, 'inicio/listar-personas.html', personas)

import requests
def crypto_price(request):
    url_binance = 'https://api.binance.com/api/v3/ticker/price'
    datos = requests.get(url_binance)
    contexto = {'precios': datos.json}
    return render(request, 'inicio/crypto_price.html', contexto)
