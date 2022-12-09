RUTA_BASE = '/home/ana/Proyectos/archivos/'
archivo = RUTA_BASE + 'datos_03.txt'

datos = [
    {'nombre':'Juan', 'apellido':'García', 'apellido2':'Romero','edad':22},
    {'nombre':'Maria', 'apellido':'Lopez', 'apellido2':'Sanchez','edad':31},
    {'nombre':'Miguel', 'apellido':'Castillo', 'apellido2':'Garzón','edad':44}
]

with open(archivo, 'a+') as f:
    for d in datos:
        cadena = f"{d['nombre']},{d['apellido']},{d['apellido2']},{d['edad']}\n"
        f.write(cadena)