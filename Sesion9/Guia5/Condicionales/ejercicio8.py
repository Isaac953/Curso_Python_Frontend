#Main
numeros = [1,5,8,1,3,1,9,4,3,5,4]
print("\nLista con duplicados")
print(numeros)

#Función para eliminar duplicados
def elimina_duplicados(lista):
  sinDuplicados = set(lista)
  new_list = list(sinDuplicados)
  return new_list

#Mostrar datos de la nueva lista 
print("\nNueva lista sin duplicados")
print(elimina_duplicados(numeros))