palabra = input("Ingrese una palabra: ").lower() #Convertir palabra a todo minusculas
palabra_invertida = ''

#Invertir palabra ingresada
for letra in palabra:
    palabra_invertida = letra + palabra_invertida

#Si palabra ingresada es igual a invertida entonces es palindromo
if palabra == palabra_invertida:
    print("Es un Palindromo")
else:
    print("No es un Palindromo")