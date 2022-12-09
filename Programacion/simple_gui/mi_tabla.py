import PySimpleGUI as sg
import csv
import os

sg.theme('LightGray1')
sg.set_options(font='Calibri 12',button_element_size=(3,2))

CSV_FILE = sg.popup_get_file(
                            'Seleccione el archivo CSV', 
                            file_types=(("Archivos CSV", "*.csv"),), 
                            initial_folder=os.path.dirname(__file__), 
                            history=True,
                            location=(400,400), )

if CSV_FILE is None:
    sg.popup_error('Cancelando')
    exit()

def read_csv_file(filename):
    data = []
    header_list = []
    if filename is not None:
        try:
            with open(filename, encoding='UTF-16') as infile:
                reader = csv.reader(infile,delimiter='\t')
                # reader = fix_nulls(filename)
                header_list = next(reader)
                try:
                    data = list(reader)  # read everything else into a list of rows
                except Exception as e:
                    print(e)
                    sg.popup_error('Error reading file', e)
                    return None, None
        except:
            with open(filename,  encoding='utf-8') as infile:
                reader = csv.reader(infile, delimiter=',')
                # reader = fix_nulls(filename)
                header_list = next(reader)
                try:
                    data = list(reader)  # read everything else into a list of rows
                except Exception as e:
                    with open(filename) as infile:
                        reader = csv.reader(infile, delimiter=',')
                        # reader = fix_nulls(filename)
                        header_list = next(reader)
                        try:
                            data = list(reader)  # read everything else into a list of rows
                        except Exception as e:
                            print(e)
                            sg.popup_error('Error reading file', e)
                            return None, None
    return data, header_list

def write_csv_file(filename, header, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)


def main():
    data, header_list = read_csv_file(CSV_FILE)

    # ------ Window Layout ------
    layout = [  [sg.Text(f'Lista de tareas', font='_ 18')],
                [sg.Text('Seleccione un registro para editarlo', pad=(20))],
                # [sg.Text(k='-RECORDS SHOWN-', font='_ 18')],
                # [sg.Text(k='-SELECTED-')],
                [sg.T('Id:'), 
                 sg.Input(k='-ID-', size=(5,1), focus=False, disabled=True),
                 sg.T('Tarea:'),
                 sg.Input(k='-EDITOR-', focus=True, disabled= True,expand_x=True),
                 sg.Checkbox('Hecho', k='-HECHO-',disabled=True)],
                 [sg.HorizontalSeparator(pad=(20))],
                [sg.B('Nuevo', key='-NUEVO-',pad=(10,20)),
                 sg.B('Guardar', key='-GUARDAR-'),
                 sg.B('Borrar', key='-BORRAR-'),sg.Push(),
                 sg.B('Cancelar', key='-CANCELAR-'),
                 sg.B('Salir', key='-SALIR-')],
                [sg.Table(
                    values=data, 
                    headings=header_list, 
                    max_col_width=25,
                    auto_size_columns=True, 
                    display_row_numbers=False, 
                    vertical_scroll_only=True,
                    justification='left', 
                    num_rows=30,
                    key='-TABLE-', 
                    selected_row_colors='black on white', 
                    enable_events=True,
                    expand_x=True, 
                    expand_y=True,
                    enable_click_events=True)],
                [sg.Sizegrip()]]

    # ------ Create Window ------
    window = sg.Window('Tabla de tareas CSV ', 
                        layout, 
                        resizable=True, 
                        finalize=True,
                        location=(400,300))
    editando = None
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, '-SALIR-'):
            break

        if event[0] == '-TABLE-' and event[2][0] not in (None,-1) :
            datos = data[event[2][0]]
            editando = event[2][0]
            window['-ID-'].update(datos[0])
            window['-EDITOR-'].update(datos[1])
            if datos[2].strip() == 'Hecho':
                window['-HECHO-'].update(True)
            else:
                window['-HECHO-'].update(False)
            
            window['-ID-'].update(disabled=False)
            window['-EDITOR-'].update(disabled=False)
            window['-HECHO-'].update(disabled=False)

        if event == '-NUEVO-':
            editando = -1
            window['-ID-'].update('')
            window['-EDITOR-'].update('')
            window['-HECHO-'].update(False)
            window['-ID-'].update(disabled=False)
            window['-EDITOR-'].update(disabled=False)
            window['-HECHO-'].update(disabled=False)

        if event == '-GUARDAR-':
            #print(values)
            if editando is not None:
                if values['-HECHO-']:
                    estado= 'Hecho'
                else:
                    estado = 'Pendiente'
                if editando == -1:
                    data.append([values['-ID-'], values['-EDITOR-'], estado])
                else:
                    data[editando] =[values['-ID-'], values['-EDITOR-'], estado]
            editando = None
            window['-ID-'].update('')
            window['-EDITOR-'].update('')
            window['-HECHO-'].update(False)

            window['-TABLE-'].update(data)
            window['-ID-'].update(disabled=True)
            window['-EDITOR-'].update(disabled=True)
            window['-HECHO-'].update(disabled=True)
            write_csv_file(CSV_FILE, header_list, data)
            
        if event == '-CANCELAR-':
            editando = -1
            window['-ID-'].update('')
            window['-EDITOR-'].update('')
            window['-HECHO-'].update(False)
            editando = None
            window['-ID-'].update(disabled=True)
            window['-EDITOR-'].update(disabled=True)
            window['-HECHO-'].update(disabled=True)

        if event == '-BORRAR-':
            if editando not in (None,-1):
                data.pop(editando)
                window['-TABLE-'].update(data)
                write_csv_file(CSV_FILE, header_list, data)

            window['-ID-'].update('')
            window['-EDITOR-'].update('')
            window['-HECHO-'].update(False)
            editando = None
            window['-ID-'].update(disabled=True)
            window['-EDITOR-'].update(disabled=True)
            window['-HECHO-'].update(disabled=True)


if __name__ == '__main__':
    main()        