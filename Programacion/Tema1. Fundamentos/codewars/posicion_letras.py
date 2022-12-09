import string

def alphabet_position(text):
    text = text.lower()
    abc = string.ascii_lowercase
    salida = []
    for s in text:
        if abc.find(s) > -1:
            salida.append(str(abc.find(s)+1))
    
    return ' '.join(salida)


print(alphabet_position("The sunset sets at twelve o' clock."))

