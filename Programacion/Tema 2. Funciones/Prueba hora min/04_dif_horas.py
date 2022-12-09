def hora_segundos_3(cadena_hora):
    return int(cadena_hora[0:2]) * 3600 + int(cadena_hora[3:5]) * 60 + int(cadena_hora[6:8])

"""
Escribir una función que reciba dos horas en formato 'hh:mm:ss'
Debe devolver la diferencia entre ellas en formato 'hh:mm:ss'
"""

def dif_horas(inicio, fin):
    diferencia = abs(hora_segundos_3(fin) - hora_segundos_3(inicio))
    h = diferencia // 3600
    m = diferencia % 3600 // 60
    s = diferencia % 3600 % 60

    return f'{h:02d}:{m:02d}:{s:02d}'

"""
1. Pasar inicio y fin a segundos usando hora_segundos
2. Restar los valores
3. Calcular horas, minutos y segundos
4. Devolver la cadena
"""

print (dif_horas('24:13:13','12:11:13'))
