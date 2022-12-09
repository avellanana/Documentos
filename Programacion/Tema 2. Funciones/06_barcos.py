import pprint

# tabla = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [3,4,5],
#     [2,7,6]
# ]

# lista = [1,2,3,4]
# lista[1] = 0
# print(lista)

# print(tabla[1][1])

# for i in range(len(tabla)):
#     for j in range(len(tabla[0])):
#         print(tabla[i][j], end= ' ')
#     print()

# for i in tabla:
#     for j in i:
#         print(j, end=' ')
#     print()




def crear_tablero():
    tablero = []
    for f in range(10):
        fila = []
        for c in range(10):
            fila.append(0)
        tablero.append(fila)
    return tablero

def pedir_barcos(tablero):
    while True:
        objetivo_f = input('Dime la fila: ')
        if objetivo_f == '':
            break
        objetivo_f = int(objetivo_f)
        objetivo_c = int(input('Dime la columna: '))
        tablero[objetivo_f][objetivo_c] = 1

def disparos(tablero):
    objetivo_f = int(input('Dime la fila: '))
    objetivo_c = int(input('Dime la columna: '))

    if tablero[objetivo_f][objetivo_c] == 1:
        print('¡¡¡TOCADO!!!')
    else:
        print('¡¡¡AGUA!!!')


def main():
    cuadro = crear_tablero()
    pedir_barcos(cuadro)
    pprint.pprint(cuadro)
    disparos(cuadro)

main()