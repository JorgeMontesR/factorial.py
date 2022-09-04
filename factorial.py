factorial = (int(input("Ingrese un numero:")))
resultado = factorial * (factorial-1)

for i in range(factorial -2, 0, -1):
    resultado = resultado * i
print(resultado)