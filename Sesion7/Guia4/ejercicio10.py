from datetime import datetime, timedelta

#Variables de datos de parqueo
precio_parqueo = 1.50

formato = "%I:%M:%S %p" #Formato para poder convertir cadena a datetime

ingreso = "07:45:00 AM" #Hora de ingreso
salida = "09:10:00 AM" #Hora de salida

pago = 0.00

#Convertir la fecha con hora de ingreso y salida en formado hh:mm:ss
ingresoc = datetime.strptime(ingreso, formato).time()
salidac = datetime.strptime(salida, formato).time()

#Restar el tiempo de salida con el de ingreso para sacar el tiempo total de parqueo
total_horas = timedelta(hours = salidac.hour - ingresoc.hour, minutes = salidac.minute - ingresoc.minute)
horas_char = str(total_horas) #Convertir resultado en un string
find_hour = horas_char.find(':') #Iterar string con find para sacar solo las horas
find_minutes = horas_char.find(':00') #Iterar string con find para sacar solo los minutos
total_horasc = int(horas_char[0:find_hour])
total_minutesc = int(horas_char[2:find_minutes])

while True:
    print('\n--Bienvenido al programa para validar ticket de parqueo--')
    print('1: Generar pago de ticket')
    print('2: Salir')
    opcion = int(input('Escriba el número de opción: '))
    if opcion == 1:
        if total_minutesc < 30:
            print(f'\nSu hora de entrada fue a las {ingresoc.strftime("%I:%M %p")} y su salida es {salidac.strftime("%I:%M %p")}')
            pago = total_horasc * precio_parqueo
            print(f'\nEl tiempo total de parqueo es: {total_horas} horas')
            print(f'El monto a pagar de parqueo es: ${pago} dólares')

            print(f'\nTicket validado')
            break
        elif total_minutesc >= 30:
            print(f'\nSu hora de entrada fue a las {ingresoc.strftime("%I:%M %p")} y su salida es {salidac.strftime("%I:%M %p")}')
            pago = (total_horasc + 1) * precio_parqueo #Si minutos es mayor a 30 entonces se cobra los $1.50
            print(f'\nEl tiempo total de parqueo es: {total_horas} horas')
            print(f'El monto a pagar de parqueo es: ${pago} dólares')

            print(f'\nTicket validado')
            break
    elif opcion == 2:
        break