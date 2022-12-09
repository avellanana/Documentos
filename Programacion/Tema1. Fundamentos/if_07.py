# ax + b = 0
# x = -b/a

a = int(input("Escribe el valor de a: "))
b = int(input("Escribe el valor de b: "))


if a == 0 and b == 0:
    print("Todos los números son solución")
else:
    if a == 0:
        print("No hay solución")
    else:
        resultado = -b/a
        print(f'Una solución {resultado}')
