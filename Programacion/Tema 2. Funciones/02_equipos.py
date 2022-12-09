import random
import pprint

alumnos = [
'Javi', 
'Jose', 
'Miguel', 
'A. Muñoz', 
'Ana', 
'A.Sanchez', 
'Luciano', 
'Juan', 
'Pablo', 
'Dani', 
'Pedro',
'P. González',
'Carlos',
'Adrián']

lista_equipos = [1,2,3,4,5,6,7,8]

def crea_equipos(gente,miembros):
    if len(gente) < miembros:
        return gente
    
    if miembros == 0:
        return []

    listas = []

#1. Calcular el numero equipos
#2. Crear las listas y llenarlas aleatoriamente
#3.  Asignar las personas restantes a los equipos

    num_equipos = len(gente) // miembros

    listas = []

    for i in range(num_equipos):
        salida = []
        for j in range(miembros):
            aleatorio = random.choice(gente)
            salida.append(aleatorio)
            gente.remove(aleatorio)
        listas.append(salida)

    for p in range(len(gente)):
        listas[p].append(gente[p])
    
    return listas

pprint.pprint(crea_equipos(alumnos,30))
