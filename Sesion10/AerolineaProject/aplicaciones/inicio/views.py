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
        'empleados': [{'nombre':'alicia', 'edad': '25', 'class': 'color1'}, {
        'nombre':'beto', 'edad': '22', 'class': 'color2'}, {'nombre':'camila', 'edad': '30', 'class': 'color1'}, 
        {'nombre':'diana', 'edad': '24', 'class': 'color2'}]
    }
    return render(request, 'inicio/lista-con-edad.html', personas)