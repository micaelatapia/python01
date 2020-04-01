"""14. Ingresar un numero de dos cifras, si es mayor que 50 mostrarlo invertido.
Sino mostrar la cifra que corresponde a las unidades"""
import math

nro = int(input("Ingresar numero de dos cifras: "))

while nro > 99:
    print("Error, no se puede tener mas de 2 digitos")
    nro = int(input("Ingresar numero de dos cifras: "))

if nro > 50:
    variabletrunc = math.trunc(nro / 10)
    nro = nro % 10
    print("El numero invertido: ", nro, variabletrunc)
else:
    print("Decimal: ", nro - nro % 10., nro % 10)