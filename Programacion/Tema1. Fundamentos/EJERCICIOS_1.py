
# print("Divisor de números")
# dividendo = int(input("Escriba el dividendo "))
# divisor = int(input("Escriba el divisor "))

# if(divisor == 0):
#     print("No se puede dividir por 0")
# else:
#     division = dividendo//divisor
#     resto = dividendo%divisor
#     if(resto == 0):
#         print("La división es exacta. Cociente: ", division)
#     else:
#         print("La división no es exacta. Cociente: ", division, "Resto: ", resto )


#EJERCICIO 2

# print("Comparador de números")
# num1 = float(input("Escribe un numero: "))
# num2 = float(input("Escribe otro numero: "))

# if(num1>num2):
#     print("Menor", num2, "; Mayor", num1)
# else:
#     if(num1==num2):
#         print("Los dos numeros son iguales")
#     else:
#         print("Menor", num1, "; Mayor", num2)


#EJERCICIO 3

# print("Comparador de años")
# actual = int(input("¿En qué año estamos? "))
# cualquiera = int(input("Escribe un año cualquiera "))
# diferencia = abs(actual - cualquiera)

# if (actual>cualquiera):
#     print(f'Desde el año {actual} han pasado {diferencia} años')
# else:
#     if(actual == cualquiera):
#         print('¡Son el mismo año!')
#     else:
#         if(diferencia == 1):
#             print(f'Para llegar al año {cualquiera} falta 1 año')
#         else:
#             print(f'Para llegar al año {cualquiera} faltan {diferencia} años')


#EJERCICIO 8
import math
print("Ejercicio de ecuación de segundo grado")

a = float(input("Escribe el coeficiente a: "))
b = float(input("Escribe el coeficiente b: "))
c = float(input("Escribe el coeficiente c: "))

x = -c/b
raiz = (b*b) - (4*a*c)

if a == 0:
    if b == 0:
        print("Sin solución")
    else:
        print("x vale: {x}")
else:
    if raiz >= 0:
        resultado1 = ((-b + math.sqrt(raiz))/2*a)
        resultado2 = ((-b - math.sqrt(raiz))/2*a)
        print(f'Las soluciones de la ecuación son {resultado1} y {resultado2}')
    else:
        print("No tiene solución")



