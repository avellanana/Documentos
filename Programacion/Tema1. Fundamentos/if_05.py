print("Comparador de múltiplos")
num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))


if(num1==0 or num2 == 0):
    print("No se puede dividir entre 0")
else:
    resto1= num1%num2
    resto2= num2%num1
    if (resto1 == 0):
        print(f'El {num1} es múltiplo de {num2}')
    else:
        if(resto2 == 0):
            print(f'El {num2} es múltiplo de {num1}')
        else:
            if(num1 > num2):
                print(f'El {num1} no es multiplo de {num2}')
            else:
                print(f'El {num2} no es multiplo del {num1}')




