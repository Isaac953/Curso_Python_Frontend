# programa para uso de funciones

n1 = int(input('Escriba el primer número: '))
n2 = int(input('Escriba el segundo número: '))

# Función
def relacion(a, b):
    if a>b:
        print(f'\nnúmero {a} mayor a número {b}')
        print(1)
    elif a<b:
        print(f'\nnúmero {a} menor a número {b}')
        print(-1)
    elif a==b:
        print(f'\nnúmero {a} igual a número {b}')
        print(0)

relacion(n1, n2)