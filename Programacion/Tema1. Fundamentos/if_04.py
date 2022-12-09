#EJERCICIO 3

print("Comparador de años")
num1 = int(input("¿En qué año estamos? "))
num2 = int(input("Escribe un año cualquiera "))

if (num1 == num2):
    print(f'Son el mismo año')
else:
    if (num1 > num2):
        resultado1 = num1-num2
        print(f'Han pasado {resultado1} años')
    else:
        if (num2 > num1):
            resultado2 = num2 - num1
            print(f'Faltan {resultado2} años por llegar')