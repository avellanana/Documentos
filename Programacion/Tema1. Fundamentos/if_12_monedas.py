numero = 17342

billetes500 = numero//500
resto500 = numero%500

billetes200 = resto500//200
resto200 = resto500%200

billetes100 = resto200//100
resto100 = resto200%100

billetes50 = resto100//50
resto50 = resto100%50

billetes20 = resto50//20
resto20 = resto50%20

billetes10 = resto20//10
resto10 = resto20%10

billetes5 = resto10//5
resto5 = resto10%5

moneda2 = resto5//2
resto2 = resto5%2

mensaje = f'Billetes de 500: {billetes500} \nBilletes de 200: {billetes200} \nBilletes de 100: {billetes100} \nBilletes de 50 {billetes50} \nBilletes de 20 {billetes20} \nBilletes de 10 {billetes10} \nBilletes de 5: {billetes5} \nMonedas de 2: {moneda2}\nMoneda de 1: {resto2}'

print(mensaje)