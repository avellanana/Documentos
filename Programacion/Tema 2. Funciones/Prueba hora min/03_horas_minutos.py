"""
Hacer una funcion que reciba una hora en formato hh:mm:ss
Debe devolver la cantidad de segundos de dicha hora
"""

# 1. Pedir las horas, minutos y segundos


def hora_segundos(cadena_hora):
    trozos_hora = cadena_hora.split(":")
    valores = []
    for i in trozos_hora:
        i = int(i)
        valores.append(i)
 
    
    segundos_hora = valores[0] * 3600
    minuto_segundo = valores[1] * 60
    segundo = valores[2]

    segundos = segundos_hora + minuto_segundo + segundo

    return segundos
    


print (hora_segundos('09:12:33'))


def hora_segundos_3(cadena_hora):
    return int(cadena_hora[0:2]) * 3600 + int(cadena_hora[3:5]) * 60 + int(cadena_hora[6:8])

print (hora_segundos_3('23:24:24'))