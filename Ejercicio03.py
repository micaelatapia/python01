"""3. Una empresa liquida sueldos según la categoría de cada empleado y paga
por hora según la siguiente tabla:
categoría 1: $150
categoría 2: $200
categoría 3: $250
categoría 4: $280
Diseñar un programa que permita ingresar la categoría de cada empleado y las
horas que trabajo en el mes y calcule:
a) Calcular el sueldo bruto y el sueldo neto (descontar 17% de aportes)
de cada empleado
b) Calcular el total de sueldos que paga la empresa
c) Determinar cuántos empleados de cada categoría hay"""

cont = 0

categoria = int(input("Ingresar el numero de categoria del empleado: "))
horas = int(input("Ingresar las horas que trabajo en el mes: "))

while categoria > 0 or categoria < 5:

    cont = cont + 1

    if categoria == 1:
        horas = horas * 150
        print("Sueldo bruto: ", horas)
        total1 = horas
        calculo = horas - (horas * 17 / 100)
        print("Sueldo neto: ", calculo)

    if categoria == 2:
        horas = horas * 200
        print("Sueldo bruto: ", horas)
        total2 = horas
        calculo1 = horas - (horas * 17 / 100)
        print("Sueldo neto: ", calculo1)

    if categoria == 3:
        horas = horas * 250
        print("Sueldo bruto: ", horas)
        total3 = horas
        calculo2 = horas - (horas * 17 / 100)
        print("Sueldo neto: ", calculo2)

    if categoria == 4:
        horas = horas * 280
        print("Sueldo bruto: ", horas)
        total4 = horas
        calculo3 = horas - (horas * 17 / 100)
        print("Sueldo neto: ", calculo3)

    categoria = int(input("Ingresar el numero de categoria del empleado: "))
    horas = int(input("Ingresar las horas que trabajo en el mes: "))

    if categoria < 1 or categoria > 4:
        totalSueldos = total1 + total2 + total3 + total4
        print("El total de sueldos que paga la empresa es: $", totalSueldos)
        print("Hay ", cont, " empleados en total")
