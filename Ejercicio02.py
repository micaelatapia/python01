"""2. Se ingresan 100 números enteros positivos, por cada número
ingresado se le solicita al operador que seleccione la operación
a realizar: si el operador ingresa 1, el programa debe devolver
el factorial  del numero ingresado; si el operador ingresa 2 el
programa debe solicitarle al operador la potencia a la cual
quiere elevar el número ingresado y debe mostrar el resultado
y para cualquier otro valor de operación el programa debe informar
si el numero ingresado es par, impar o nulo."""

cont = 0
acum = 0
fact = 1

op = int(input("Seleciones la operacion a realizar,1 o 2: "))

while cont < 5:
    cont = cont + 1
    acum = acum + fact
    while op == 1:
        nro = int(input("Ingresar numero: "))
        if nro >= 0:
            for I in range(1, nro):
                fact = fact * I
            print("El resultado es: ", fact)
            cont = 0
            acum = 0
            op = int(input("Seleciones la operacion a realizar,1 o 2: "))

    while op == 2:
        nro = int(input("Ingresar numero: "))
        potencia = int(input("ingrese la potencia para elevar el número: "))
        print("El numero elevado es: ", nro ** potencia)
        op = int(input("Seleciones la operacion a realizar,1 o 2: "))

    while op >= 3:
        nro = int(input("Ingresar numero: "))
        if nro % 2:
            print("El numero es nulo")
        else:
            print("El numero es par")