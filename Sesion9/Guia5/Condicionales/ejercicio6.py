agenda_dic = {} #Diccionario vacio

while True:
    #Opciones a elegir
    print("\n--Bienvenido a la Agenda--")
    print("1. Añadir/modificar")
    print("2. Listar")
    print("3. Salir")

    opcion = int(input("Escriba el número de opción: "))

    #Agregar y módificar
    if opcion == 1:
        nombre = input("Nombre del contacto: ")
        #Verificar si nombre existe, mostrar con cual número de telefono esta    
        if nombre in agenda_dic:
            print("%s Ya existe su número de teléfono es %s" % (nombre,agenda_dic[nombre]))
            opcion = input("Pulsa 'm' si quieres modificarlo. Otra tecla para continuar. ")
            #Modificar número si se presiona m
            if opcion == "m":
                numero = input("Escriba el nuevo número de télefono: ")
                agenda_dic[nombre]=numero
        #Si nombre no existe simplemente se agregan los datos
        else:
            numero = input("Escriba el número de télefono: ")
            agenda_dic[nombre]=numero
    #Listar contactos
    elif opcion == 2:
        for nombre, numero in agenda_dic.items():
            print(nombre,"->",numero)
    #Salir
    elif opcion == 3:
        break
    else:
        print("Opción incorrecta")
        break