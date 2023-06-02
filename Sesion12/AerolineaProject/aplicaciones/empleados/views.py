from django.shortcuts import render
from .models import Empleado
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def listar_empleados(request):
    lista = {'lista':Empleado.objects.all(),'titulo':'Lista de Empleados'}
    print(lista)
    return render(request, 'empleados/listar-empleados.html',lista)

class CrearEmpleado(CreateView):
    template_name = 'empleados/crear-empleado.html'
    model = Empleado
    fields = ['nombre', 'correo', 'sueldo']
    success_url = reverse_lazy('empleados_app:listar-empleados')
