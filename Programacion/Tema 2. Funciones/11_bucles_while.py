control = 0
mensaje = 'este es un experimento de while'

exit()
while control < len(mensaje) -1:
    control += 1
    if mensaje[control] == 'e':
        continue
    print(mensaje[control])


print('He salido del bucle')

# break
# continue
# exit