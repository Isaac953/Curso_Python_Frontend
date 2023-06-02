print('Calcular el sueldo semanal de una persona')

#Pedir datos por teclado de nombre, dui, horas_t
nombre = input('Digite el nombre: ')
dui = input('Digite el número de DUI: ')
horas_t = int(input('Digite las horas trabajadas: '))

pago = 10.00 #Pago hora normal
sueldo = 0.00
horas_extra = 0
pago_extra = 0.00
sueldo_extra = 0.00

if horas_t <= 40:
    #Calcular sueldo
    sueldo = pago * horas_t
    print(f'El sueldo de la persona {nombre} con DUI {dui} es de: ${sueldo} dólares')
elif horas_t > 40:
    #Calcular sueldo extra
    horas_extra = horas_t - 40
    pago_extra = 200 * pago/100 #El pago por hora extra es al 200%
    sueldo_extra = pago_extra * horas_extra

    #Calcular sueldo
    horas_t = horas_t - horas_extra
    sueldo = (pago * horas_t) + sueldo_extra
    print(f'El sueldo de la persona {nombre} con DUI {dui} es de: ${sueldo} dólares')