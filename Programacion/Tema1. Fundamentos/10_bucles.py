#Dos tipos de bucle, por contador (sabemos cuantas vueltas dará el bucle - FOR), y los bucles que se ejecutan por una condicion (mientras sea cierta - WHILE).

# for variable (inicio, fin, salto)

for i in range(50,20,-2):
    print(f'La i vale {i}')




import pprint

lista = []

for i in range(20):
    lista.append(f'Elemento {i}')

pprint.pprint(lista)





#for i in range(len(lista)):
#    print (lista[i])




largo = len(lista)

for i in range(largo):
    print (lista[i])


for x in lista:
    print(x)