"""
3. Modifica el programa anterior de tal forma que los caracteres utilizados en el perímetro
del rectángulo sean caracteres producto (*) y el interior esté vacío.


base = 5
altura = 4
espacios = 3

print('*'*base)
print('*' + ' '*espacios +'*')
print('*' + ' '*espacios + '*')
print('*'*base)
"""



base2 = 5
espacios2 = 3

linea_base = '*' * base2
linea_media = '*' + ' '*(base2 - 2) + '*'

print(linea_base)
print(linea_media)
print(linea_media)
print(linea_media)
print(linea_media)
print(linea_base)



base = 5
altura = 4

lineabase = '\t*' * base
lineamedia = '\t*' + '\t '*(base-2) + '\t*'

print(lineabase)
for i in range(altura):
    print(lineamedia)
print(lineabase)

