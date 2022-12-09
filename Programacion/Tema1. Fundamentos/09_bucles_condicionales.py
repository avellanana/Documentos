numero = int(input('Dime un número: '))

if numero == 0:
    print('El número es cero')
elif numero > 0:
    print('El número es mayor que cero')
else:
    print('El número es menor que cero')


# Es lo mismo
numero2 = int(input('Dime otro número: '))

if numero2 == 0:
    print('El número2 es cero')
else:
    if numero2 > 0:
        print('El número2 es mayor que cero')
    else:
        print('El número2 es menor que cero')



## OPERADORES ##


"""
#Operadores aritméticos
+
-
*
/

** Exponente 2**5
// División entera
% Módulo (el resto de la división entera)

#Operadores de comparación
>
<
==
!= Distinto 
>=
<=
---------------------------------------------------

#Operadores de asignación o incremento

+=
-=
*=
/=
//=
%=
**=

x = 1
x = x + 1
x += 1



"""

num3 = int(input ("Escribe un numero: "))
if num3%2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El número {numero} es impar")