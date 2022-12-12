"""Escribe una funcion que reciba como parametro una cadena de texto y devuelva una lista con las vocales que haya en dicha cadena"""

# def vocales(cadena):
#     vocales = ['a','e','i','o','u']
#     lista = []

#     for i in cadena:
#         if i.lower() in vocales and i.lower() not in lista:
#             lista.append(i)

#     return lista

# print(vocales('Escriba'))

"""
Funcion que reciba una cadena y devuelva una cadena con los códicos ascii de las letras

A=65
B=66
C=67

'ABC' --> '65 66 67'

"""


# def ascii(cadena):
#     lista_ascii = []

#     for letra in cadena:
#         lista_ascii.append(str(ord(letra)))
    
#     return ' '.join(lista_ascii)
# cad= 'ABC'
# print(ascii(cad))


def ascii_txt(cadena):
    lista_cadena = []
    salida = ''
    cadena = cadena.split(' ')

    for numero in cadena:
        salida += chr(int(numero))
    return salida

print(ascii_txt('65 66 67'))
