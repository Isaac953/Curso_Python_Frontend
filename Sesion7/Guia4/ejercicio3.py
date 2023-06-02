from decimal import Decimal

print('Programa para conversión de monedas')
print('1: Dólar')
print('2: Colón')
print('3: Bitcoin')

try:
    opcion = int(input('Escriba el número de opción: '))
    if opcion == 1:
        print('Por favor elija la conversión')
        print('1: Dolar a colon')
        print('2: Dolar a Bitcoin')
        conversion_opcion = int(input('Escriba el número de opción: '))
        if conversion_opcion == 1:
            precio = 8.75
            cantidad = float(input('Escriba la cantidad a convertir: '))
            conversion = cantidad * precio
            print(f'La cantidad de {cantidad} USD en colon es: {conversion} SVC')
        elif conversion_opcion == 2:
            precio = 0.00004089
            cantidad = float(input('Escriba la cantidad a convertir: '))
            conversion = Decimal(cantidad * precio)
            print(f'La cantidad de {cantidad} USD en bitcoin es: {round(conversion, 10)} BTC')

    elif opcion == 2:
        print('Por favor elija la conversión')
        print('1: Colon a Dolar')
        print('2: Colon a Bitcoin')
        conversion_opcion = int(input('Escriba el número de opción: '))
        if conversion_opcion == 1:
            precio = 0.1144
            cantidad = float(input('Escriba la cantidad a convertir: '))
            conversion = cantidad * precio
            print(f'La cantidad de {cantidad} SVC en dolar es: {conversion} USD')
        elif conversion_opcion == 2:
            precio = 0.000004677
            cantidad = float(input('Escriba la cantidad a convertir: '))
            conversion = Decimal(cantidad * precio)
            print(f'La cantidad de {cantidad} SVC en bitcoin es: {round(conversion, 10)} BTC')

    elif opcion == 3:
        print('Por favor elija la conversión')
        print('1: Bitcoin a Dolar')
        print('2: Bitcoin a Colon')
        conversion_opcion = int(input('Escriba el número de opción: '))
        if conversion_opcion == 1:
            precio = Decimal(24452.89)
            cantidad = Decimal(input('Escriba la cantidad a convertir: '))
            conversion = cantidad * precio
            print(f'La cantidad de {cantidad} BTC en dolar es: {round(conversion, 2)} USD')
        elif conversion_opcion == 2:
            precio = Decimal(213834.41)
            cantidad = Decimal(input('Escriba la cantidad a convertir: '))
            conversion = cantidad * precio
            print(f'La cantidad de {cantidad} BTC en SVC es: {round(conversion, 2)} SVC')

    else:
        print('No valido')
except ValueError:
    print('Por favor escriba un número')
except KeyboardInterrupt:
    print('Ha finalizado el programa')