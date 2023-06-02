from django.shortcuts import render

# Create your views here.
def func_index(request):
    captura_datos = {
        'titulo': 'Captura de Datos',
    }
    return render(request, 'captura_datos/datos.html', captura_datos)

# Create your views here.
def result_data(request):
    dt1 = request.POST["dt1"],
    dt2 = request.POST["dt2"],
    dt3 = request.POST["dt3"],
    dt4 = request.POST["dt4"],
    if dt1[0] != '':
        resultdiv = 'Con datos'
        resultbtn = 'disabled'

    captura_datos = {
        'titulo': 'Captura de Datos',
        'datos': [{'nombre': 'Mathematics', 'valor': dt4[0], 'class': 'color1' }, {'nombre': 'Chemistry', 'valor': dt3[0], 'class': 'color2' },
                  {'nombre': 'Physics', 'valor': dt2[0], 'class': 'color1' }, {'nombre': 'Name', 'valor': dt1[0], 'class': 'color2' }],
        'div': resultdiv,
        'btn': resultbtn,
    }
    return render(request, 'captura_datos/datos.html', captura_datos)
