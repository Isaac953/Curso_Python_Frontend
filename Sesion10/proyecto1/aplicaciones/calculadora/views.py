from django.shortcuts import render

# Create your views here.
def func_index(request):
    calculadora = {
        'titulo': 'Calculadora',
    }
    return render(request, 'calculadora/calc.html', calculadora)

# Create your views here.
def math(request):
    num1 = request.POST["num1"],
    num2 = request.POST["num2"],
    operation = request.POST["calc"],

    if str(operation[0]) == "suma":
        result = int(num1[0]) + int(num2[0])
        resultdiv = 'Con datos'
        resultbtn = 'disabled'
    elif str(operation[0]) == "resta":
        result = int(num1[0]) - int(num2[0])
        resultdiv = 'Con datos'
        resultbtn = 'disabled'
    elif str(operation[0]) == "multiplicacion":
        result = int(num1[0]) * int(num2[0])
        resultdiv = 'Con datos'
        resultbtn = 'disabled'
    elif str(operation[0]) == "division":
        result = int(num1[0]) / int(num2[0])
        resultdiv = 'Con datos'
        resultbtn = 'disabled'

    calculadora = {
        'titulo': 'Calculadora',
        'numero1': num1[0],
        'numero2': num2[0],
        'operacion': operation[0],
        'resultado': result,
        'div': resultdiv,
        'btn': resultbtn,
    }
    return render(request, 'calculadora/calc.html', calculadora)
