lista_inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

#Función añadir precio
def anadir_precio(lista_inmuebles):
    precio = (lista_inmuebles['metros'] * 1000 + lista_inmuebles['habitaciones'] * 5000 + int(lista_inmuebles['garaje']) * 15000) * (1 - (2020 - lista_inmuebles['año']) / 100)
    if lista_inmuebles['zona'] == 'B':
        precio *= 1.5
    lista_inmuebles['precio'] = precio
    return lista_inmuebles

#Función buscar inmuebles
def buscar_inmuebles(lista_inmuebles, presupuesto):
    def filtro(lista_inmuebles):
        return lista_inmuebles['precio'] <= presupuesto
    return list(filter(filtro,map(anadir_precio, lista_inmuebles)))

resultado = buscar_inmuebles((lista_inmuebles), 115000)

#Iterando resultado de función buscar_inmuebles
for inmueble in resultado:
    print(f"Año: {inmueble['año']}, Metros: {inmueble['metros']}, Habitaciones: {inmueble['habitaciones']}, Garaje: {inmueble['garaje']}, Zona: {inmueble['zona']}, Precio: {inmueble['precio']}")