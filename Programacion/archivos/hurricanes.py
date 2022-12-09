def limpiar(fila):
    salida = []
    for elem in fila:
        elem = elem.replace('"','').strip()
        elem = elem.replace('\n','')
        salida.append(elem)
    return salida

# x=['"Month"', ' "Average"', ' "2005"', ' "2006"', ' "2007"', ' "2008"', ' "2009"', ' "2010"', ' "2011"', ' "2012"', ' "2013"', ' "2014"', ' "2015"\n']
# print(limpiar(x))


ruta_base = '/home/ana/Proyectos/archivos/'
datos = ruta_base + 'hurricanes.csv'

huracanes = []

archivo = open(datos,'r')
cabeceras = archivo.readline()
claves = limpiar(cabeceras.split(','))

for linea in archivo:
    fila = limpiar(linea.split(','))
    d = {}
    for i in range(len(fila)):
        d[claves[i]] = fila[i]

    huracanes.append(d)

import pprint

pprint.pprint(huracanes)



