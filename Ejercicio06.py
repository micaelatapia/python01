"""6. Una empresa conoce para cada empleado los siguientes datos:
 Nombre
 Sueldo
 Categoría
Hay 100 empleados, distribuidos en 3 categorías (1, 2 y 3)
Diseñar un programa que permita ingresar los datos de todos los empleados
y calcular:
a) Total de sueldos que paga la empresa (en $)
b) Cantidad de empleados que ganan más de $20000
c) Cantidad de empleados que ganan menos de $5000 y cuya categoría sea 1
d) Nombre del empleado que gana más y cuál es su sueldo
e) Total de sueldos (en $) de cada categoría """

acumSueldo = 0
contSueldo = 0
cont5k = 0
acumCategoria1 = 0
acumCategoria2 = 0
acumCategoria3 = 0

nombre = input("Ingresar nombre: ")
sueldo = int(input("Ingresar sueldo: "))
categoria = int(input("Ingresar categoria 1, 2 o 3: "))
maximo = sueldo
maxNombre = 0

while categoria == 1 or categoria == 2 or categoria == 3:
    acumSueldo = acumSueldo + sueldo

    if sueldo > 20000:
        contSueldo = contSueldo + 1

    if categoria == 1 and sueldo < 5000:
        cont5k = cont5k + 1

    if categoria == 1:
        acumCategoria1 = acumCategoria1 + sueldo

    if categoria == 2:
        acumCategoria2 = acumCategoria2 + sueldo

    if categoria == 3:
        acumCategoria3 = acumCategoria3 + sueldo

    if sueldo > maximo:
        maximo = sueldo
    if maximo == sueldo:
        maxNombre = nombre

    nombre = input("Ingresar nombre: ")
    sueldo = int(input("Ingresar sueldo: "))
    categoria = int(input("Ingresar categoria 1, 2 o 3: "))

print("Total de sueldos que paga la empresa: $", acumSueldo)
print("Cantidad de empleados que ganan más de $20000: ", contSueldo)
print("Cantidad de empleados que ganan menos de $5000 y cuya categoría sea 1: ", cont5k)
print("Nombre del empleado que gana más y cuál es su sueldo: ", maxNombre,
"y su sueldo es de: $", maximo)
print("El total de sueldos: categoria 1: $", acumCategoria1,
    "categoria 2: $", acumCategoria2, "categoria 3: $", acumCategoria3)


