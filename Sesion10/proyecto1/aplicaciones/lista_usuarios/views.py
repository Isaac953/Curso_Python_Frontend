from django.shortcuts import render

# Create your views here.
def func_index(request):
    users = [{'nombre':'Alicia', 'usuario': '92alice', 'edad': '25'}, 
             {'nombre':'Beto', 'usuario': 'beto83', 'edad': '22'}, 
             {'nombre':'Camila', 'usuario': 'camila12', 'edad': '30'}, 
             {'nombre':'Diana', 'usuario': '92diana92', 'edad': '24'}, 
             {'nombre':'Ingrid', 'usuario': 'ingrid12', 'edad': '23'},
             {'nombre':'Isaac', 'usuario': 'isaac7', 'edad': '29'},
             {'nombre':'Rosa', 'usuario': '25rosa', 'edad': '25'}]
    #Recorrer la lista en la llave usuario
    for i in range(len(users)):
        cadena = users[i]['usuario']
        sl = slice(1)
        #Comprobando si inicia con número o letra el usuario
        if(cadena[sl] >= '0' and cadena[sl] <= '9'): #Se toma la primera letra del string
            users[i]['class'] = 'text-normal' #Agregar class css
        else:
            users[i]['class'] = 'text-bold' #Agregar class css

    lista_usuarios = {
        'titulo': 'Lista de Usuarios',
        'user_list': users
    }
    return render(request, 'lista_usuarios/lista-usuarios.html', lista_usuarios)