anio = int(input('Digite el año: '))
if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0): 
    print(f'El anio {anio} es bisiesto')
else:
    print(f'El anio {anio} no es bisiesto')