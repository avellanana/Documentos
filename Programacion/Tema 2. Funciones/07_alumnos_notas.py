def alumno_notas(alumno, *asignaturas):
    print(f'El alumno {alumno} se ha matriculado de las asignaturas:')
    print('----------')
    for a in asignaturas:
        print(a)

alumno_notas('Miguelito de la Roda', 'Programación', 'BD', 'Sistemas', 'Filosofía')
print()

def alumno_notas(alumno, *asignaturas, **notas):
    print(f'El alumno {alumno} se ha matriculado de las asignaturas: ')
    print('-----------')
    for a in asignaturas:
        print(a)

asig = ['Programación', 'BD', 'Sistemas']
alumno_notas('Miguelito', *asig)

print()
print()

def alumno_notas_2(alumno, *asignaturas, **notas):
    print(f'El alumno {alumno} se ha matriculado de las asignaturas: ')
    print('-----------')
    for a in asignaturas:
        print(a)
    
    # for n in notas:
    #     print(f' {n} : {notas[n]}')

    for k,v in notas.items():
        print(f' {k}: {v}')

alumno = 'Miguelito'

asig = ['Programacion', 'BD', 'Sistemas', 'Filologia']

notas = {'Programación':7, 'BD':2.5, 'Sistemas':5}

alumno_notas_2(alumno, *asig, **notas)

