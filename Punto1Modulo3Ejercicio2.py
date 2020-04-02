NumeroSemana = int(input("Ingrese numero de semana: "))
GastoSemanal = int(input("Ingrese gasto semanal: "))

if NumeroSemana < 5:
    print("El gasto semanal es de: $", GastoSemanal * 7 / 100)

while NumeroSemana <= 0 or NumeroSemana > 5:
    print("Error, ingrese un numero de semana correcto")
    NumeroSemana = int(input("Ingrese numero de semana: "))
    GastoSemanal = int(input("Ingrese gasto semanal: "))

    if NumeroSemana < 5:
        print("El gasto semanal es de: $", GastoSemanal * 7 / 100)

while NumeroSemana <= 4:
    NumeroSemana = int(input("Ingrese numero de semana: "))
    GastoSemanal = int(input("Ingrese gasto semanal: "))

    if NumeroSemana < 5:
        print("El gasto semanal es de: $", GastoSemanal * 7 / 100)