from datetime import datetime, timedelta

# Ingreso de datos
dia = input('Ingrese el día: ')
print('\nMeses del año')
#Diccionario de meses
dict_meses = {'01': 'Enero', 
              '02': 'Febrero', 
              '03': 'Marzo', 
              '04': 'Abril', 
              '05': 'Mayo', 
              '06': 'Junio', 
              '07': 'Julio',
              '08': 'Agosto',
              '09': 'Septiembre',
              '10': 'Octubre',
              '11': 'Noviembre',
              '12': 'Diciembre'}
#Imprimir el resultado para que elija el número de mes
for llave,valor in dict_meses.items():
	print (llave,":",valor)
mes = input('Ingrese el número de mes: ')
anio = input('Ingrese el año: ')

#Convertir String en Fecha
date_string = dia + ' ' + mes + ', ' + anio
date_object = datetime.strptime(date_string, "%d %m, %Y").date()

fecha_actual = date_object.strftime("%d-%B-%Y")
print(f'\nLa fecha ingresada es {fecha_actual}') #Fecha actual

suma_dias = int(input('Ingrese la cantidad de dias a sumar: '))

#Ciclo while para sumar fechas
i = 1
while i <= suma_dias:
  fecha_sumada = date_object + timedelta(days = i)#Suma de horas
  i += 1
fecha_format = fecha_sumada.strftime("%d-%B-%Y")

print(fecha_format)