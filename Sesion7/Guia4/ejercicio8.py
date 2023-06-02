print('\n--Bienvenido al programa calcular alquiler de vehiculos--')
#variables
monto_fijo = 30.00
cantidad_kilometros = int(input('\nEscriba la cantidad de kilometros recorridos de su auto: '))
monto_neto = 0.00
monto_adicionalt = 0.00
monto_adicionalm = 0.00
cantidad_kilometros_t = 0
cantidad_kilometros_m = 0
monto_iva = 0.00
monto_total = 0.00

#Condición menor o igual a 300 km
if cantidad_kilometros <= 300:
    monto_neto = monto_fijo
    monto_iva = monto_neto * 0.13 #Calcular IVA
    monto_total = monto_neto + monto_iva #Monto total con IVA incluido

    print(f'\nEl monto a pagar de alquiler por {cantidad_kilometros} km recorridos es de:')
    print(f'Monto Neto: ${round(monto_neto, 2)} dólares')
    print(f'Monto IVA: ${round(monto_iva, 2)} dólares')
    print(f'Monto Total: ${round(monto_total, 2)} dólares')

#Condición mayor a 300 km y menor o igual a 1000 km
elif cantidad_kilometros > 300 and cantidad_kilometros <= 1000:
    cantidad_kilometros_t = cantidad_kilometros - 300 #Restar el exceso de 300 km para sacar los km a $0.25
    monto_adicionalt = cantidad_kilometros_t * 0.25 #Monto adicional por cada km arriba de 300
    monto_neto = monto_fijo + monto_adicionalt #Suma de monto fijo con monto adicional 
    monto_iva = monto_neto * 0.13 #Calcular IVA
    monto_total = monto_neto + monto_iva #Monto total con IVA incluido

    print(f'\nEl monto a pagar de alquiler por {cantidad_kilometros} km recorridos es de:')
    print(f'Monto Neto: ${round(monto_neto, 2)} dólares')
    print(f'Monto IVA: ${round(monto_iva, 2)} dólares')
    print(f'Monto Total: ${round(monto_total, 2)} dólares')

#Condición mayor a 1000 km
elif cantidad_kilometros > 1000:
    cantidad_kilometros_m = cantidad_kilometros - 1000 #Restar el exceso de 1000 km para sacar los km a $0.50
    monto_adicionalm = cantidad_kilometros_m * 0.50 #Monto adicional por cada km arriba de 1000
    cantidad_kilometros_t = 1000 - 300 #Restar el exceso de 300 km para sacar los km a $0.25
    monto_adicionalt = cantidad_kilometros_t * 0.25 #Monto adicional por cada km arriba de 300
    monto_neto = monto_fijo + monto_adicionalt + monto_adicionalm #Suma de monto fijo con monto adicional 
    monto_iva = monto_neto * 0.13 #Calcular IVA
    monto_total = monto_neto + monto_iva #Monto total con IVA incluido

    print(f'\nEl monto a pagar de alquiler por {cantidad_kilometros} km recorridos es de:')
    print(f'Monto Neto: ${round(monto_neto, 2)} dólares')
    print(f'Monto IVA: ${round(monto_iva, 2)} dólares')
    print(f'Monto Total: ${round(monto_total, 2)} dólares')