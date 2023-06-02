sueldo = int(input('Digite su sueldo: '))
isr = 0 #impuesto sobre la renta
isss = round(sueldo * 0.03, 2) #Abajo de sueldo $1000
afp = round(sueldo * 0.0725, 2)
porcentaje = 0
sg = round(sueldo - isss - afp, 2) #Sueldo gravable

#Tramo I
if(sueldo <= 472):
    print('El ISSS es de: $', isss, 'dólares')
    print('El AFP es de: $', afp, 'dólares')
    print('El sueldo gravable es de: $', sg, 'dólares')
    print('El impuesto sobre la renta es: $', isr, 'dólares, sin retención')
#Tramo II
elif(sueldo > 472 and sueldo <= 895.24):
    porcentaje = 0.10
    isr = round((sueldo - 472)*porcentaje + 17.67, 2)
    print('El ISSS es de: $', isss, 'dólares')
    print('El AFP es de: $', afp, 'dólares')
    print('El sueldo gravable es de: $', sg, 'dólares')
    print('El impuesto sobre la renta es: $', isr, 'dólares')
#Tramo III
elif(sueldo > 895.24 and sueldo <= 2038.10):
    porcentaje = 0.20
    if(sueldo < 1000):
        isr = round((sueldo - 895.24)*porcentaje + 60.00, 2)
        print('El ISSS es de: $', isss, 'dólares')
        print('El AFP es de: $', afp, 'dólares')
        print('El sueldo gravable es de: $', sg, 'dólares')
        print('El impuesto sobre la renta es: $', isr, 'dólares')
    elif(sueldo > 1000):
        isss = round(1000 * 0.03, 2) #tope del ISSS
        isr = round((sueldo - 895.24)*porcentaje + 60.00, 2)
        print('El ISSS es de: $', isss, 'dólares')
        print('El AFP es de: $', afp, 'dólares')
        print('El sueldo gravable es de: $', sg, 'dólares')
        print('El impuesto sobre la renta es: $', isr, 'dólares')
#Tramo IV
elif(sueldo > 2038.10):
    isss = round(1000 * 0.03, 2) #tope del ISSS
    isr = round((sueldo - 2038.10)*porcentaje + 288.57, 2)
    print('El ISSS es de: $', isss, 'dólares')
    print('El AFP es de: $', afp, 'dólares')
    print('El sueldo gravable es de: $', sg, 'dólares')
    print('El impuesto sobre la renta es: $', isr, 'dólares')
