"""16. Ingresar dos números y sin resolver la multiplicación mostrar una
leyenda según el producto sea negativo, positivo o cero"""


nro1 = int(input("Ingresar un numero: "))

nro2 = int(input("Ingresar otro numero: "))

if nro1 > 0 and nro2 > 0:
    print("El numero es positivo")

if nro1 > 0 and nro2 < 0:
    print("El numero es negativo")

if nro1 < 0 and nro2 < 0:
    print("El numero es positivo")

if nro1 < 0 and nro2 > 0:
    print("El numero es negativo")

if nro1 == 0 and nro2 > 0:
    print("El numero es 0")

if nro1 > 0 and nro2 == 0:
    print("El numero es 0")

if nro1 < 0 and nro2 == 0:
    print("El numero es 0")

if nro1 == 0 and nro2 < 0:
    print("El numero es 0")

if nro1 == 0 and nro2 == 0:
    print("El numero es 0")