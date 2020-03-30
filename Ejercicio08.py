"""8. En un negocio de venta de chocolate hay tres tipos de chocolate:
amargo, dulce y con almendras. El amargo cuesta $20 el kg, el dulce $25
y con almendras $30 el kg. Por cada venta, ingresan al sistema:
 Nombre del vendedor (Pedro o Pablo – se ingresa como texto)
 cantidad de chocolate vendido (en kg).
 Tipo de chocolate(1.amargo, 2.dulce, 3.con almendras)
 Día del mes ( 1 a 30 – nunca trabajan los 31)
Cuando se llega a día =31, quieren ver:
a) Qué día del mes se registró la mayor venta (en Kg.) y quién realizó la venta
b) Qué día del mes se registró la mayor venta (en $) y quién realizó la venta.
c) Quién facturó más.
d) Cantidad de Kg. vendidos por tipo de chocolate.
e) Porcentaje de ventas de Pedro en relación al total."""

acum_amargo = 0
acum_dulce = 0
acum_almendras = 0

promedioPedro = 0

dia_del_mes = int(input("Ingresar dia del mes del 1 al 30: "))
nombre_vendedor = input("Quien es el vendedor, pedro o pablo: ")
cantidad_vendido = int(input("Ingrese cantidad (kg) de chocolates vendidos: "))
tipo_chocolate = int(input("Ingrese el tipo de chocolate 1.amargo 2.dulce 3.almedras: "))

mayor_venta_kg = cantidad_vendido
vendedor_kg = nombre_vendedor
dia_mayor_kg = dia_del_mes

mayorVentaPesos = cantidad_vendido
diaMayorGanancia = dia_del_mes
vendedor = nombre_vendedor

totalSuma1 = 0
totalSuma2 = 0
totalSuma3 = 0

totalSumaPedro1 = 0
totalSumaPedro2 = 0
totalSumaPedro3 = 0
totalSumaPablo1 = 0
totalSumaPablo2 = 0
totalSumaPablo3 = 0
nomMayorFactura = nombre_vendedor
sumaTotalPablo = 0
sumaTotalPedro = 0


while dia_del_mes != 31:
    if cantidad_vendido > mayor_venta_kg:
        mayor_venta_kg = cantidad_vendido

    if mayor_venta_kg == cantidad_vendido:
        vendedor_kg = nombre_vendedor
        dia_mayor_kg = dia_del_mes
        vendedor = nombre_vendedor

    if cantidad_vendido > mayorVentaPesos:
        mayorVentaPesos = cantidad_vendido
    if mayorVentaPesos == cantidad_vendido:
        diaMayorGanancia = dia_del_mes

    if tipo_chocolate == 1:
        acum_amargo = acum_amargo + cantidad_vendido
        totalSuma1 = acum_amargo * 20

    if tipo_chocolate == 2:
        acum_dulce = acum_dulce + cantidad_vendido
        totalSuma2 = acum_dulce * 25

    if tipo_chocolate == 3:
        acum_almendras = acum_almendras + cantidad_vendido
        totalSuma3 = acum_almendras * 30

    if nombre_vendedor == "pablo":
        if tipo_chocolate == 1:
            totalSumaPablo1 = cantidad_vendido * 20
        if tipo_chocolate == 2:
            totalSumaPablo2 = cantidad_vendido * 25
        if tipo_chocolate == 3:
            totalSumaPablo3 = cantidad_vendido * 30
        sumaTotalPablo = totalSumaPablo1 + totalSumaPablo2 + totalSumaPablo3

    if nombre_vendedor == "pedro":

        if tipo_chocolate == 1:
            totalSumaPedro1 = cantidad_vendido * 20
        if tipo_chocolate == 2:
            totalSumaPedro2 = cantidad_vendido * 25
        if tipo_chocolate == 3:
            totalSumaPedro3 = cantidad_vendido * 30
        sumaTotalPedro = totalSumaPedro1 + totalSumaPedro2 + totalSumaPedro3
        promedioPedro = (sumaTotalPedro + sumaTotalPablo) / sumaTotalPedro * 100

    if sumaTotalPedro > sumaTotalPablo:
        if nombre_vendedor > nomMayorFactura:
            nomMayorFactura = nombre_vendedor

    if sumaTotalPablo > sumaTotalPedro:
        if nombre_vendedor > nomMayorFactura:
            nomMayorFactura = nombre_vendedor

    dia_del_mes = int(input("ingresar dia del mes del 1 al 30 :"))
    if dia_del_mes != 31:
        nombre_vendedor = input("Quien es el vendedor, pedro o pablo: ")
        cantidad_vendido = int(input("Ingrese cantidad (kg) de chocolates vendidos: "))
        tipo_chocolate = int(input("ingrese el tipo de chocolate 1.amargo 2.dulce 3.almedras: "))

print("Se entrego la mayor cantidad de kg el dia: ", dia_mayor_kg ,"y el nombre del vendedor es: ", vendedor_kg )
print("El dia con mayor ganancia en $ es el dia: ", diaMayorGanancia, "el nombre del vendedor es: ", vendedor)
print("La cantidad de kg vendidos del sabor amargo es de: ", acum_amargo, "kg")
print("La cantidad de kg vendidos del sabor dulce es de: ", acum_dulce, "kg")
print("La cantidad de kg vendidos del sabor almendras es de: ", acum_almendras, "kg")
print("Facturo mas: ", nomMayorFactura)
print("Porcentaje de ventas de Pedro en relacion al total: ", promedioPedro, "%")