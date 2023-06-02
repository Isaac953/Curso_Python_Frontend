# programa con funciones de validar email

email = input('Ingrese su dirección de email: ')

# Función
def validar_email(em):
    if em.find('@') >= 0:
        print(f'El email "{em}" es valido')
    elif em.find('@') < 0:
        print(f'El email "{em}" no es valido')

validar_email(email)