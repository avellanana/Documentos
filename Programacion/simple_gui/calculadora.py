import PySimpleGUI as ps

menu_temas = ['menu',
            ['LightTeal', 'LightYellow','Material1','Material2','Tan']
            ]

def crear_ventana(tema):
    ps.theme(tema)
    boton_size = (6,3)
    ps.set_options(font='Calibri 12')

    layout = [
        [ps.Text('0.0',
        font = 'Courier 20',
        justification='right',
        expand_x=True, 
        right_click_menu = menu_temas,
        pad=(30,50),
        key='-TEXTO-')],
        [ps.Button('Clear', expand_x=True, size=boton_size), 
        ps.Button('Enter', expand_x=True, size=boton_size, disabled = True)],
        [
            ps.Button('7', size=boton_size),
            ps.Button('8', size=boton_size),
            ps.Button('9', size=boton_size),
            ps.Button('*', size=boton_size)
        ],
            [
            ps.Button('4', size=boton_size),
            ps.Button('5', size=boton_size),
            ps.Button('6', size=boton_size),
            ps.Button('/', size=boton_size)
        ],
            [
            ps.Button('1', size=boton_size),
            ps.Button('2', size=boton_size),
            ps.Button('3', size=boton_size),
            ps.Button('-', size=boton_size)
        ],
            [
            ps.Button('0', expand_x=True, expand_y=True),
            ps.Button('.', size=boton_size),
            ps.Button('+', size=boton_size)
        ]
    ]
    return ps.Window('Calculadora',layout)

tema_defecto = 'Topanga'
window = crear_ventana(tema_defecto)

numeros = []
operaciones = []

while True:
    event, values = window.read()
    if event == ps.WIN_CLOSED:
        break
    if event in menu_temas[1]:
        window.close()
        window = crear_ventana(event)
    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        numeros.append(event)
        num_string = ''.join(numeros)
        window['-TEXTO-'].update(num_string)
        window['Enter'].update(disabled=False)
    
    if event in ['+','-','*','/']:
        operaciones.append(''.join(numeros))
        operaciones.append(event)
        numeros = []
        window['-TEXTO-'].update('')
    
    if event == 'Enter':
        operaciones.append(''.join(numeros))
        resultado = eval(''.join(operaciones))
        window['-TEXTO-'].update(f'{resultado}')
        operaciones = []
        numeros = [str(resultado)]
        window['Enter'].update(disabled=True)
    
    if event == 'Clear':
        window['-TEXTO-'].update('0.0')
        numeros = []
        operaciones = []
        window['Enter'].update(disabled=True)

window.close()