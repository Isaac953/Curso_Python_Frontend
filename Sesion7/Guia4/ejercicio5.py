from datetime import datetime, timedelta

while True:
    print('\n--Bienvenido al programa sumar hora actual del reloj--')
    print('1: Ingresar hora actual del reloj')
    print('2: Salir')
    opcion = int(input('\nEscriba el número de opción: '))

    if opcion == 1:
        fecha_completa = datetime.today() #Hora actual con fecha
        hora_actual = fecha_completa.strftime("%I:%M %p") #Convertir fecha a horas
        fecha_actual = fecha_completa.strftime("%d-%m-%Y") #formatear fecha

        print(f'La hora actual es: {hora_actual} del día {fecha_actual}') #Hora actual

        suma_hora = int(input('\nEscriba las horas a sumar: '))#Número de horas a sumar

        total_horas = fecha_completa + timedelta(hours = suma_hora)#Suma de horas
        total_horasc = total_horas.strftime("%I:%M %p")#Nueva hora en formato
        nueva_fecha = total_horas.strftime("%d-%m-%Y")#Nueva fecha en caso que la suma supere al día
        print(f'En {suma_hora} horas el reloj marcara las: {total_horasc} del día {nueva_fecha}') #Resultado

        break
    elif opcion == 2:
        break