# programa para uso de sets
equipos = {'Barcelona', 'Real Madrid', 'Manchester City', 'Juventus', 'Munich'}
print(len(equipos))
# Son DESordenados
print(equipos)
# NO son indexadas
# print(equipos[0])
# Son inmutabes
# equipos[0] = 'Dortmund'
# Son dimanicos
equipos.add('Aguila')
print(equipos)
equipos.discard('Juventus')
print(equipos)

for equipo in equipos:
    print(f'Equipo: {equipo}')

# no acepta repetidos
equipos.add('Munich')
print(equipos)