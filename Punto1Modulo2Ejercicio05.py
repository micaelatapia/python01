import math

nro = int(input("Ingrese un numero de 3 cifras: "))

while nro < 99:
    nro = int(input("Error, escribir numero de 3 cifras: "))


while nro > 999:
    nro = int(input("Error, escribir numero de 3 cifras: "))

variableTrunc = math.trunc(nro / 10) % 10

print("El segundo numero es: ", variableTrunc)