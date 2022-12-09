# Esto es un comentario

# Definimos una variable


saludo = "Hola k ase"
print(saludo[0] + saludo[1] , 'kkkk')

saludo.casefold()

cadena = "En un lugar de la Mancha..."
print(cadena)
print(len(cadena))

print(cadena.capitalize())
print(cadena.swapcase())
print(cadena.replace('la', 'lo'))

print(cadena.title())

print(cadena.split())
trozos = cadena.split('a')
print(trozos)

cadena = '1,2,3,4,5,6,7'
trozos = cadena.split(',')
print(trozos)

unida = '\n'.join(trozos)
print(unida)
print(cadena + unida)

cadena = '1,2,3,4,5,6,7,8'
trozos = cadena.split(',')
print(trozos)
trozos[3] = 'hola'
print(trozos)
