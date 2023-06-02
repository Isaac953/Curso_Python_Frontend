dict_p = {} #Diccionario vacio
frase = 'arbol verde arbol naranja arbol amarillo' #Frase
lista_palabras = frase.split(" ") #Separar palabras

#Recorrer lista
for palabra in lista_palabras:
	if palabra in dict_p:
		dict_p[palabra]+=1 #Si se repite palabra se va sumando
	else:
		dict_p[palabra]=1	

#Función para imprimir llave y valor del diccionario
def recibir_cadena(dict_p):
    for llave,valor in dict_p.items():
	    print (llave,":",valor)
	    
recibir_cadena(dict_p)