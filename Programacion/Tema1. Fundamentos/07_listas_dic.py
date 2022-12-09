#LISTAS
import pprint

mi_lista = [1,2,3,4,'hola',True,['a','b','c']]
mi_lista.append('otro')
mi_lista.extend([7,8,9])
mi_lista.insert(4,'nuevo dato')

mi_lista = mi_lista + ['k','l','m'] + [1,4,7]
x = mi_lista.pop()
print(mi_lista)
print(x)

lector = mi_lista[5]
print('Lector: ', lector)
print(mi_lista)

c = mi_lista[4]
print('c: ',c)
print(mi_lista)


#TUPLAS#

mi_tupla = (1,2,3,19,1,2,1)
largo = len(mi_tupla)
elem = mi_tupla.count(1)
elem3 = mi_tupla[3]
print('Largo: ', largo)
print('Elem: ', elem)
print('Tercero: ', elem3)
print(list(mi_tupla))


#Las tuplas se pueden definir poniendo coma la final:
mt = (1,)


# DICCIONARIOS #

mi_dict = {
    '1':1, '2':4, '3':9, '4':16, '5':25
}

mi_dict['6'] = 36

print (mi_dict)
print (mi_dict['6'])

# mi_dict = dict()

persona1 = {
    'nombre' : 'Paco_1',
    'dni' : '1234567L'
}

persona2 = {
    'nombre' : 'Paco_2',
    'dni' : '1234456L'
}

personas = {
    1: persona1,
    2: persona2
}

pprint.pprint(personas)