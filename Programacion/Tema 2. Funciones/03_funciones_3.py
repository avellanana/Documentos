def suma(a,b):
    return a + b

# print(suma(1.9,2.21),'hola','otra','otra mas')

def suma_muchos(separador, *args):
    total = 0
    for i in args:
        total += i

    return total

print(suma_muchos(1,2,3,4,5,6,7,8,12,21,21))


def encadenar(separador, *args):
    """
    Concatena las cadenas contenidas en args y las separa con el separador
    """
    cadena = ""
    for i in range (len(args)):
        cadena = separador.join(args)
    return (cadena)
    
print(encadenar('--','lunes','martes','miercoles'))

#VERSION MAS SIMPLIFICADA
def encadenar2(separador, *args):
    return separador.join(args)

print(encadenar2('-*-','lunes','martes','miercoles'))


#VERSION COMPLETA

def encadenar3(separador, *args):
    """
    Concatena las cadenas contenidas en args y las separa con el separador
    separador: caracteres para separar cadenas
    *args: lista de cadenas
    """
palabras = []
while True:
    entrada = input('Dime una palabra: ')
    if entrada == ' ':
        break
    else:
        palabras.append(entrada)

sep = input('Dime un separador: ')
print(encadenar3(sep,*palabras))