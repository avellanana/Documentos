# def esto_falla():
#     try:
#         f= open('no_existe.txt','r')
#         print('----_TRY-----')
#     except FileNotFoundError as e:
#         print(e)
#     else:
#         print('--------else---------')
#     finally:
#         print('------finally--------')

# esto_falla()


def genera_error(num):
    if num < 10:
        raise Exception('Error de numero demasiado pequeño')
    else:
        print('Funciona!!')

try:
    genera_error(9)
except:
    exit()