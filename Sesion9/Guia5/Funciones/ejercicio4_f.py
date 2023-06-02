#Función para aplicar descuento
def aplicar_descuento(precio, descuento):
    return precio - precio * descuento / 100
    
#Función para aplicar IVA
def aplicar_iva(precio, porcentaje):
    return precio + precio * porcentaje / 100

#Función cesta de compra
def cesta_compra(cesta, function):
    total = 0
    for precio, descuento in cesta.items():
        total += function(precio, descuento)
    return total

print('El precio compra tras aplicar los descuentos es: $', cesta_compra({500:10, 650:15, 230:5}, aplicar_descuento))
print('El precio compra tras aplicar el IVA es: $', cesta_compra({500:10, 650:15, 230:5}, aplicar_iva))