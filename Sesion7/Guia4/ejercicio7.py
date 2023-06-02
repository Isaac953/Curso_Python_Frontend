print('\n--Bienvenido al programa calcular oferta de producto--')
#Variables
descuento = 0.00
total_descuento = 0.00
productos_docena = 0
precio_unitario = 1.50 #Precio de $1.50 pensado por mi
precio = 0.00
precio_con_descuento = 0.00
unidades_regalo = 0
cantidad_docena = int(input('\nEscriba la cantidad de docenas que quiere comprar: '))

if cantidad_docena <= 3:
    productos_docena = cantidad_docena * 12 #Sacar total de productos por docena
    precio = precio_unitario * productos_docena #Precio sin descuento
    descuento = 0.10 #Descuento del 10% 
    total_descuento = precio * descuento #Sacando el descuento en dólares
    precio_con_descuento = precio - total_descuento #Precio total restandole el descuento
    print(f'\nEl monto de la compra es: ${round(precio, 2)} dólares')
    print(f'El monto del descuento del 10% es: ${round(total_descuento, 2)} dólares')
    print(f'El monto a pagar es: ${round(precio_con_descuento, 2)} dólares')
    print(f'Usted ha realizado la compra de {cantidad_docena} docenas equivalente a {productos_docena} productos')
elif cantidad_docena > 3:
    productos_docena = cantidad_docena * 12 #Sacar total de productos por docena
    precio = precio_unitario * productos_docena #Precio sin descuento
    descuento = 0.15 #Descuento del 15% 
    total_descuento = precio * descuento #Sacando el descuento en dólares
    precio_con_descuento = precio - total_descuento #Precio total restandole el descuento
    unidades_regalo = cantidad_docena - 3 #Se resta las primeras 3 docenas
    print(f'\nEl monto de la compra es: ${round(precio, 2)} dólares')
    print(f'El monto del descuento del 15%  es: ${round(total_descuento, 2)} dólares')
    print(f'El monto a pagar es: ${round(precio_con_descuento, 2)} dólares')
    print(f'Usted ha realizado la compra de {cantidad_docena} docenas equivalente a {productos_docena} productos con {unidades_regalo} unidades de obsequio')
