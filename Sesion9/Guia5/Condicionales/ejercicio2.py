#Calcular potencia
base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))
resultado = 1

#Exponente 0 y positivos
if exponente >= 0:
    for _ in range(exponente):
        resultado *=base
    print(f'El resultado de {base} elevado a la {exponente} es: {resultado}')
#Exponente negativo
elif exponente < 0:
    resultado = base ** exponente
    print(f'El resultado de {base} elevado a la {exponente} es: {resultado}')
