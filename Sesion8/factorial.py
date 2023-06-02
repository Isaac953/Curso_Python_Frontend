# Programa para calcular el factorial de un numero
# 5! = 5x4x3x2x2 = 120

n = int(input('digite un numero: '))

f = n
for i in range(1, n):
    f *= i # f = f * i

print(f'el factorial de {n} es: {f}')