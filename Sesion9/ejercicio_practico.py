# programa para uso de diccionarios
list_empleados = []
while True:
    print('\n---Programa para agregar empleados---')
    print('1: Agregar empleado')
    print('2: Imprimir lista')
    print('3: Salir')

    opcion = int(input('Escriba el número de opción: '))

    # opción 1 agregar empleado
    if opcion == 1:
        nombre = input('Escriba el nombre: ')
        cargo = input('Escriba el cargo: ')
        sueldo = float(input('Escriba el sueldo: '))
        empleado = {'nombre': nombre, 'cargo': cargo, 'sueldo': sueldo}
        list_empleados.append(empleado)
        print("Datos del empleado agregados")
    # opción 2 imprimir lista
    elif opcion == 2:
        for empleado in list_empleados:
            print(f"Nombre: {empleado['nombre']}, Cargo: {empleado['cargo']}, Sueldo: {empleado['sueldo']}")
    # opción 3 salir
    elif opcion == 3:
        break