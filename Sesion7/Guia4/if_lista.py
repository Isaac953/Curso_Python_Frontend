lista_user = [{'nombre':'alicia', 'usuario': '92alice', 'edad': '25'}, {
        'nombre':'beto', 'usuario': 'beto83', 'edad': '22'}, {'nombre':'camila', 'usuario': '12camila', 'edad': '30'}, 
        {'nombre':'diana', 'usuario': 'diana92', 'edad': '24'}, {'nombre':'isaac', 'usuario': 'isaac7', 'edad': '29'},
        {'nombre':'rosa', 'usuario': '25rosa', 'edad': '25'}]

for i in range(len(lista_user)):
    cadena = lista_user[i]['usuario']
    print(lista_user[i]['usuario'])
    sl = slice(1)
    print(cadena[sl])

    if(cadena[sl] >= '0' and cadena[sl] <= '9'):
        lista_user[i]['class'] = 'text-normal'
        print("It is a Number")
    else:
        lista_user[i]['class'] = 'text-bold'
        print("It is Not a Number")

print(lista_user)
