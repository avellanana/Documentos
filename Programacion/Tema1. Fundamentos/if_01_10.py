numero = 100003
km = numero//100_000
restokm = numero % 100_000
m = restokm//100
restom = restokm % 100

mensaje = f'Nuestro numero {numero} es \n {km} kilómetros \n {m} metros \n {restom} centímetros'

print(mensaje)

