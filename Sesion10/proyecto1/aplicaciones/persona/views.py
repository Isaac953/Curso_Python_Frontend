from django.shortcuts import render

# Create your views here.
def func_index(request):
    personas = {
        'titulo': 'Persona',
    }
    return render(request, 'persona/index.html', personas)

# Create your views here.
def mostrar_nombre_edad(request, nombre, edad):
    resultado = {
        'titulo': 'Persona',
        'nombre': nombre,
        'edad': edad,
    }
    return render(request, 'persona/index.html', resultado)