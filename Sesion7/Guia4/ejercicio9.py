print('\n--Bienvenido al programa calcular el promedio de prácticas--')

#Ingresar las 4 notas por teclado
n1 = int(input('Escriba la nota 1: '))
n2 = int(input('Escriba la nota 2: '))
n3 = int(input('Escriba la nota 3: '))
n4 = int(input('Escriba la nota 4: '))
notas = [n1, n2, n3, n4] #Almacenarlas en una lista
notas.sort() #Ordenar notas de menor a mayor
nota_eliminada = notas[0] #Capturar nota elminada
notas.pop(0) #Eliminar la nota más baja

if notas.__len__() == 3:
    promedio = (notas[0] + notas[1] + notas[2])/3 #Sacar promedio
    print(f'\nLas notas ingresadas son: {n1}, {n2}, {n3}, {n4}')
    print(f'La nota elminada es: {nota_eliminada}')
    print(f'El promedio de prácticas es: {round(promedio, 2)}')
else:
    pass