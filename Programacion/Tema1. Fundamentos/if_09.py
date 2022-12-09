entrada = input('¿Quieres calcular el área de un círculo o de un triángulo? Responde C o T: ')
from cmath import pi
import math

if entrada == 'C':
    radio = float(input('Escribe el radio del circulo: '))
    areac = math.pi*radio**2
    print(f'El area es {areac}')
elif entrada == 'T':
    base = float(input('Escribe la base: '))
    altura = float(input('Escribe la altura: '))
    areat = (base*altura)/2
    print(f'El area es {areat}')
else:
    print('Entrada no valida')


