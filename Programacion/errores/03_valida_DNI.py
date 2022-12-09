"""
letras_validas: TRWAGMYFPDXBNJZSQVHLCKE
dani VALIDO:
    - Longitud de 8
    - La letra será válida si el índice coincide con el resto de la división entera del número entre 23
"""
LETRAS = 'TRWAGMYFPDXBNJZSQVHLCKE'

def calcula_letra(dni):
    indice = dni%23
    letra = LETRAS[indice]
    return letra

def valida_dni(dni):

    return len(dni) == 9 and calcula_letra(int(dni[:8])) == dni[8].upper()

print(valida_dni('55000173C'))
