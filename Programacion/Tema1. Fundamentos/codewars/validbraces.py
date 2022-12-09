def validbraces(cadena):
    if len(cadena) % 2 == 1:
        return False

    parejas = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    valores = list(parejas.values())

    pila = []
    for s in cadena:
        if s in valores:
            pila.append(s)
        else:
            if pila == []:
                return False
            ultimo = pila.pop()
            if ultimo != parejas[s]:
                return False
    
    return pila == []

print(validbraces('(()){{]]'))


