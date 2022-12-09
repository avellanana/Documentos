import PySimpleGUI as ps

"""
1. Establecer el tema
2. Crear el layout
3. Event loop
4. Cerrar la ventana
"""

#1
ps.theme('GreenMono')

#2
layout = [
    [ps.Text('Introduce tu nombre')],
    [ps.InputText()],
    [ps.Button('OK'), ps.Button('Cancel')],
    [ps.Radio('Kokoko','nada')],[ps.Radio('Wuwuwu','nada')],[ps.Radio('Lalala','nada')],
    [ps.Checkbox('jijiji')]
]

#3
window = ps.Window('Formulario',layout)

while True:
    event, values = window.read()
    if event == 'Cancel' or event == ps.WIN_CLOSED:
        break
    if event == 'OK':
        print(values[0])

window.close()

#4
