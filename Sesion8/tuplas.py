lenguajes = ('Python', 'C++', 'PHP', 'Perl', 100, (2,3,4))
print(len(lenguajes))
print(lenguajes)
print(lenguajes[0])
# NO son mutables
# lenguajes[2] = 'C#'
# son estaticas
# lenguajes.append(1)

for lenguaje in lenguajes:
    print(f'Lenguajes: {lenguaje}')