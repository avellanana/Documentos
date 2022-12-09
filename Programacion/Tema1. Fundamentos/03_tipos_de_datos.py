#Tipos mutables

from cgi import print_arguments


numero = 0

numero = 1

cadena = 'hola'


#Tipos inmutables


#entrada
#cadena = 'Esto es un experimento con cadenas'


#separar = cadena.split()
#print(separar)
#palabra = print(separar[3])



#separar cada palabra
#ir a la posicion 4
#cambiarla a mayuscula
#juntar todas las palabras


# 1. Encontrar la palabra 'experimento'
# 2. Poner 'experimento' en mayúsculas -- upper()

cadena = 'Esto es un experimento con cadenas'

palabra = 'experimento'
longitud = len(palabra)
punto1=cadena.find(palabra)
punto2=punto1+longitud
print(punto1)
print(punto2)

parte1 = cadena[:punto1]
parte2 = palabra.upper()
parte3=cadena[punto2:]

resultado = parte1 + parte2 + parte3
print(resultado)


cadena2= 'Esto es otro experimento'
lista2 = cadena2.split()
print(lista2)
lista2[3]='EXPERIMENTO'
print(lista2)
cadenafinal=' '.join(lista2)
print(cadenafinal)


prueba = 'Prueba numero 3'
separar = prueba.split()
print(separar)

posicion = prueba.find('3')
print(posicion)

