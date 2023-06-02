from django.shortcuts import render

# Create your views here.
def func_index(request):
    return render(request, 'inicio/index.html')

def listar_personas(request):
    personas = {
        'titulo': 'Lista de personas',
        'nombres': ['alicia', 'beto', 'camila', 'diana']
    }
    return render(request, 'inicio/listar-personas.html', personas)

def listar_edad(request):
    personas = {
        'titulo': 'Lista de personas con edad',
        'empleados': [{'nombre':'alicia', 'edad': '25'}, {'nombre':'beto', 'edad': '22'}, {'nombre':'camila', 'edad': '30'}, {'nombre':'diana', 'edad': '24'}]
    }
    return render(request, 'inicio/lista-con-edad.html', personas)