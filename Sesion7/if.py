# programa para uso de condiciones simples y anidadas
# captura de datos por teclado
# conversion de cadena a entero
edad = input('Digite su edad: ')
print('su edad es:', edad)
print('tipo de edad:', type(edad))

# conversion de edad a entero
aux_edad = int(edad)
# verificar el tipo de aux_edad
print('tipo de aux_edad:', type(aux_edad))

if aux_edad>18:
    print('es adulto')
    print('Es mayor de edad')
    if aux_edad>60:
        print('y es de la tercera edad')
else:
    print('es menor de edad')

print('fin de programa... adios')