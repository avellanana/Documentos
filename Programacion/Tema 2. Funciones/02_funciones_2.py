#funcion es un bloque de código que hace algo, se le pone un nombre y se puede reutilizar. Cada funcion debe hacer 1 sola cosa. Las funciones deben tener alta cohesion 
# y bajo aclopamiento. Fuerte acomplamiento es cuando depende de que la información esté presentada de cierta forma, en cierto sitio.
#

# def saluda(persona):
#     nombre = persona
#     print(f'Hola, {nombre}')

# saluda('Alejandro')




# def saluda(persona):
#     print(f'Hola, {persona}')

# saluda('Ana')



# def saluda(personas):
#     for p in personas:
#         print(f'Hola, {p}')

# gente =['Ana', 'Miguel', 'Dani']
# saluda(gente)
# #saluda(personas = gente)



# a = 0
# print(type(a))

# a = 'hola'
# print(type(a))



def saluda(kiwi):
    salida = []
    for p in kiwi:
        salida.append(f'Hola, {p}')
    
    return salida


gente = ['Ana', 'Miguel', 'Dani']
saludos = saluda(gente)
print(saludos)


#FUNCION QUE SUME DOS NUMEROS Y DEVUELVE UN RESULTADO
def suma(a, b):
    return a + b

resultado = suma(1,2)
print (resultado)
