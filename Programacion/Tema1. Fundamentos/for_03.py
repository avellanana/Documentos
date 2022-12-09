
"""
medida = 5
simbolo = '*\t'
for i in range(1,medida):
    print(simbolo * i)


medida = 4
simbolo = '*\t'
for i in range(medida,0,-1):
    print(simbolo * i)

---

numero = 4
espacios = 3
caracteres = 1

print('.'*espacios + '*'*caracteres + '.'*espacios)
espacios -= 1
caracteres += 2
print('.'*espacios + '*'*caracteres + '.'*espacios)


numero = int(input('Dime cuantas filas quieres: '))
espacios = numero-1
caracteres = 1
for i in range(numero):
    print('\t'*espacios + '*\t'*caracteres)
    espacios -= 1
    caracteres += 2
"""

numero2 = int(input('Dime cuantas filas quieres: '))
caracteres2 = numero2*2-1
espacios2 = 0
for i in range(numero2):
    print('\t'*espacios2 + '*\t'*caracteres2)
    espacios2 += 1
    caracteres2 -= 2