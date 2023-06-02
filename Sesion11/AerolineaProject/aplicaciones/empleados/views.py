from django.shortcuts import render

# Create your views here.
def func_empleados(request):
    return render(request, 'empleados/empleados.html')