# prorama para uso de operadores lógicos y de comparación
a = 10
b = 5
c = 15
print(a<b and c>=a or a!=b)
# 0 and 1 or 1
# 0 or 1
# 1
print(a<b and (c>=a or a!=b))
# 0 and (1 or 1)
# 0 or 1
# 1
print(not False)
