# list_n = [2, 45, 12, 37, 19]
list_n = []
cant_numeros = int(input('Ingrese la cantidad de números a ingresar: '))

for n in range(cant_numeros):
    numero = int(input('Ingrese un número: '))
    list_n.append(numero)
print("Lista desordenada")
print(list_n)

for r in range(1, len(list_n)):
    for p in range(len(list_n) - r):
        if list_n[p] > list_n[p + 1]:
            list_temp = list_n[p]
            list_n[p] = list_n[p + 1]
            list_n[p + 1] = list_temp
print("Lista ordenada")
print(list_n)

print(f'El mayor es: {list_n[cant_numeros - 1]}')
print(f'El menor es: {list_n[0]}')
print(f'La sumatoria es: {sum(list_n)}')
print(f'El promedio es: {sum(list_n)/len(list_n)}')