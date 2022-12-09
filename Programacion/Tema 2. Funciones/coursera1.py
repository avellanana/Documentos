"""
tenemos un texto y hay que 
- limpiar el texto de signos de puntuacion
- eliminar palabras no relevantes (3 letras o menos)
- contabilizar palabras del texto en un diccionario
- devolver el diccionario

1. Pasar a minusculas
2. Quitar signos de puntuacion
3. Ignorar palabras de 3 letras o menos
4. Dividir la cadena por palabras
5. Procesar la cadena

"""

import string 
import pprint

txt = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

def frecuencias(texto):
    salida = {}
    texto = texto.lower()
    puntuacion = list(string.punctuation)

    for p in puntuacion:
        texto = texto.replace(p,'')
    
    palabras = texto.split()

    for palabra in palabras:
        if len(palabra) > 3:
            if salida.get(palabra) == None:
                salida[palabra] = 1
            else:
                salida[palabra] += 1
    
    return pprint.pprint(salida)

frecuencias(txt)

