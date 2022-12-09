"""
0 a 5 suspenso, 
5 a 7 aprobado,
7 a 9 notable,
+9 sobresaliente
"""

calificacion = int(input("Escribe una calificacion: "))
if calificacion < 5:
    print("La calificación es SUSPENSO")
else:
    if calificacion < 7:
        print("La calificación es APROBADO")
    else:
        if calificacion < 9:
            print("La calificación es NOTABLE")
        else:
            print("La calificación es SOBRESALIENTE")



calificacion2 = float(input("dime un numerito"))
resultado = ''

if calificacion2 < 5:
    resultado = 'SUSPENSO'
else:
    if calificacion2 < 7:
        resultado = 'APROBADO'
    else:
        if calificacion2 < 9:
            resultado = 'NOTABLE'
        else:
            resultado = 'SOBRESALIENTE'

print(resultado)
