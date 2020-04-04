cont = 0
acum = 0

nros = int(input("Ingrese 10 numeros mayores que 3 y menores que 8: "))
if nros <= 3 or nros >= 8:
    nros = int(input("Error, ingresar un numero mayor que 3 y menor que 8: "))

while cont <= 9:
    cont = cont + 1
    acum = acum + nros

    while nros <= 3 or nros >= 8:
        nros = int(input("Error, ingresar un numero mayor que 3 y menor que 8: "))

    if nros == 4:
        print("Cuatro(4)")
    if nros == 5:
        print("Cinco(5)")
    if nros == 6:
        print("Seis(6)")
    if nros == 7:
        print("Siete(7)")

    nros = int(input("Ingrese 10 numeros mayores que 3 y menores que 8: "))