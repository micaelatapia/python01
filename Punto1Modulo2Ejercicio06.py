nro = int(input("Ingresar numero: "))
raiz = nro ** (1 / 2)

if nro > 0:
    print("La raiz del numero es: ", raiz)

if nro < 0:
    print("El numero elevado es: ", nro ** 2)

if nro == 0:
    print("Error. Ha ingresado un valor nulo")