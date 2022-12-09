def opcionales(oblig_1, oblig_2, opc_1='uno',opc_2='dos', *args, **kwargs):
    print(args)
    print(kwargs)

opcionales(1,2,'a','b','c', mates = 10, lengua = 2, fisica = 9)