import pprint
monedas = [500,200,100,50,20,10,5,2,1]
numero = 17_342

desglose = {}


for m in monedas:
    desglose[m] = (numero//m)
    numero = numero % m

pprint.pprint(desglose)


for k,v in desglose.items():
    if v > 0:
        if(k<3):
            print(f'{v} moneda de {k}')
        elif(k>3):
            print(f'{v} billetes de {k}')