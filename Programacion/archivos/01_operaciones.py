#r, w, a, 
# w+ (si existe se borra o limpia; si no existe se crea), 
# r+ (si no existe, da un error), 
# a+ (si no existe, lo crea; si no existe, se añaden los datos al final), 
# b (lo abre en modo binario)

ruta_base = '/home/ana/Proyectos/archivos/'
ruta_imagenes = ruta_base + 'images/'

archivo = open(ruta_base + 'pruebas.txt','r')
numeros = []

for linea in archivo:
    numeros.append(int(linea))

archivo.close()
print(numeros)