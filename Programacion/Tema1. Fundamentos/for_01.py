
"""
for i in range(1,20,4):
    print(f'{i}\t',end='')



for i in range(1,11,1):
    print(f'{i}\t', end='')
print()
for i in range(2,21,2):
    print(f'{i}\t',end='')
print()
for i in range(20,48,3):
    print(f'{i}\t', end='')
print()
for i in range(10,31,4):
    print(f'{i}\t', end='')
print()
for i in range(40,-1,-5):
    print(f'{i}\t', end='')
print()




for i in range(2,21):
    if(i % 2 == 0):
        print(f'{i}\t', end='')
print()
"""

for i in range(20,49):
    if i % 3 == 0:
        i -= 1
        print(f'{i}\t', end='')

print()


contador = 20
for i in range(1,11):
    print(f'{contador}\t', end='')
    contador += 3

print()

cadena = ''
for i in range(20,49):
    if i % 3 == 0:
        i -= 1
        cadena += str(i) + '\t'
print(cadena)

print()

cadena = []
for i in range(20,49):
    if i % 3 == 0:
        i -= 1
        cadena.append(str(i))
resultado = cadena[::-1]

print(cadena)
print('\t'.join(resultado))