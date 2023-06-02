def titulo(cadena):
    nueva=""
    inicioPalabra=True #Inicio de la palabra
    for caracter in cadena:
        if not caracter.isalpha():
            nueva=nueva+caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva=nueva+caracter.upper()
                inicioPalabra=False  #No es inicio de la palabra
            else:
                nueva=nueva+caracter.lower()
    return nueva

print(titulo('compLejO es mEjOr qUe comPlicado'))