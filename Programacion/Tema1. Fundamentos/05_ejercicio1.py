#Entrada: Pedimos un número al usuario
#Salida:
#Imprimir: "El doble de <20> son <40>"
#          "El cuadrado de <20> son <400>"


num = int(input("Escribe un numero: "))

#Salida:
multiplicado = num*2
cuadrado = num*num

print('El doble de '+ str(num) + ' es ' + str(multiplicado))
print('El cuadrado de ' + str(num) +' es '+ str(cuadrado))



#INTERPOLACION
numero = 100
doble = numero*2
elevado = numero*numero
mensaje = f'El doble de {numero} es {doble}'
mensaje2 = f'El cuadrado de {numero} es {elevado}'
print(mensaje)
print(mensaje2)