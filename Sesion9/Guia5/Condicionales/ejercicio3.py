#Contar palabras en cadena
texto = 'El lapiz tiene tinta'
txt_list = texto.split(' ') #Separar las palabras en una lista

# default separator: space
result = len(txt_list) #Contar con len la longitud de la lista

print(texto)
print("Aca hay " + str(result) + " palabras.")