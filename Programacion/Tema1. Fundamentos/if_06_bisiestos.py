anio = int(input('Introduce un año: '))

if(anio%400 == 0):
    print(f'El año {anio} es un año bisiesto porque es múltiplo de 400')
else:
    if(anio%100 == 0):
        print(f'El año {anio} no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400')
    else:
        if(anio%4==0):
            print(f'El año {anio} es un año bisiesto porque es múltiplo de 4')
        else:
            print(f'El año {anio} no es un año bisiesto')