"""Leer el número de mes y mostrar cuantos días tiene ese mes(año actual)"""
mes = int(input("Ingrese un mes: "))

while mes <= 12 and mes >= 0:

    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("El mes tiene 31 dias")

    if mes == 2:
        print("El mes 2 (febrero) tiene 29 dias")

    if mes == 4 or mes == 9 or mes == 11:
        print("El mes tiene 30 dias")

    if mes <= 0 or mes >= 13:
        mes = int(input("Error, ingresar un numero de mes correcto"))

    mes = int(input("Ingrese un mes: "))
