#De una lista de palabras,
#encontrar la más larga e imprimirla

palabras = ['hola', 'adiós', 'manzana', 'pera', 'pin']

print(palabras[0])
print(len(palabras[0]))

# resultado = ''
# for i in palabras:
#     if(len(palabras[i])>len(palabras[i+1])):
#         resultado = len(palabras[i])
#     else:
#         resultado = len(palabras[i+1])
#         print(resultado)


indice_max = -1
max_len = 0

for i in range (len(palabras)):
    largo = len(palabras[i])
    print(largo)
    if largo > max_len:
        indice_max = i
        max_len = largo

print(palabras[indice_max])