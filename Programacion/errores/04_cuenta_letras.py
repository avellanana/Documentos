"""
Hacer un programa que pida al usuario una serie de caracteres.
Cuando termine le debe mostrar una lista con las vocales y otra con las consonantes,
además decirle cuantas hay de cada una.
Los caracteres que no son letras se descartan.
"""

    
vocales = 'a,e,i,o,u'
consonantes = 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z'

lista_consonantes = []
lista_vocales = []

#     while True:
#         entrada = input("Escriba la cadena: ")
#         if entrada == "":
#             break
#         contadorv= 0
#         contadorc= 0

#         for i in entrada:
#             lista = []
#             if i in entrada == vocales:
#                 for j in entrada:
#                     if i == j:
#                         contadorv += 1
#                 resultado = lista.append(i)
    
#             return resultado

# print(contador_caracteres())
            

while True:
    letra = input('Dime una letra: ')
    if letra == '':
        break
    if letra.lower() in consonantes:
        lista_consonantes.append(letra)
    elif letra.lower() in vocales:
        lista_vocales.append(letra)

print(f'Consonantes: {len(lista_consonantes)}')
print(lista_consonantes)

print(f'Vocales: {len(lista_vocales)}')
print(lista_vocales)
    
            




