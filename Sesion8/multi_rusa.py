# Multiplicacion Rusa

n1 = int(input('digite el primer numero: ')) # multiplicador
n2 = int(input('digite el segundo numero: ')) # multiplicando
suma = 0
while n1>=1:
    if n1%2 != 0:
        suma = suma + n2
    n1 = n1 // 2
    n2 = n2 * 2
print(f'La multiplicacion es: {suma}')