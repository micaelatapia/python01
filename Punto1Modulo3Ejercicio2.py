"""2) Calcular el promedio semanal de gastos en un mes, ingresando como datos:
 Semana número
 Gasto semanal
El proceso termina cuando “semana número” es igual a 5"""
cont = 0



NumeroSemana = int(input("Ingrese numero de semana: "))
GastoSemanal = int(input("Ingrese gasto semanal: "))


while NumeroSemana <= 0 or NumeroSemana > 5:
    cont = cont + 1
    print("Error, ingrese un numero de semana correcto")
    NumeroSemana = int(input("Ingrese numero de semana: "))
    GastoSemanal = int(input("Ingrese gasto semanal: "))
