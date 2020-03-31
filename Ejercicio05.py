"""5. Una  empresa textil desea procesar sus ventas.
 Cada vez que una persona realiza una compra se le entrega una
 factura donde consta:
  Nro. de Factura
  Código de artículo
  Cantidad del artículo
  Precio Unitario
 En cada factura se registra solamente un código de artículo y los códigos de
 artículos pueden ser 1, 3, 5 y 7.
  Diseñar un programa que permita el Ingreso de los datos y calcular:

     a) Total de cada factura
     b) Total general facturado
     c) Cantidad vendida (en unidades) para cada uno de los artículos.
     d) Total de artículos vendidos
     e) Cantidad de facturas emitidas para cada uno de los artículos.
     f) Nro. de factura con mayor valor ( en $ )
     g) Nro. de artículo con menor cantidad pedida ( por factura, "no" el total)
  h) Porcentaje de ventas (en pesos) de cada uno de los artículos sobre el total.
La entrada de datos finaliza con un número de factura igual a cero"""

cont1 = 0
cont3 = 0
cont5 = 0
cont7 = 0

totalFactura = 0
acumTotal = 0

acumArt1 = 0
acumArt3 = 0
acumArt5 = 0
acumArt7 = 0

sumaArt = 0

totalFinalFactura1 = 0
totalFinalFactura3 = 0
totalFinalFactura5 = 0
totalFinalFactura7 = 0

nroFactura = int(input("Ingresar numero de factura: "))
codArticulo = int(input("Ingresar codigo de articulo entre 1, 3 ,5 o 7: "))
cantidadArticulo = int(input("Ingresar cantidad del articulo: "))
precioUnitario = int(input("Ingresar precio unitario: "))

maxPesos = precioUnitario
maxNroFactura = nroFactura

minCodArt = codArticulo
minCantArt = cantidadArticulo

while nroFactura != 0:

    if codArticulo == 1:
        cont1 = cont1 + 1
        acumArt1 = acumArt1 + cantidadArticulo
    if codArticulo == 3:
        cont3 = cont3 + 1
        acumArt3 = acumArt3 + cantidadArticulo
    if codArticulo == 5:
        cont5 = cont5 + 1
        acumArt5 = acumArt5 + cantidadArticulo
    if codArticulo == 7:
        cont7 = cont7 + 1
        acumArt7 = acumArt7 + cantidadArticulo
    sumaArt = acumArt1 + acumArt3 + acumArt5 + acumArt7

    totalFactura = cantidadArticulo * precioUnitario
    acumTotal = acumTotal + totalFactura
    print("Total de la factura: $", totalFactura)

    if precioUnitario > maxPesos:
        maxPesos = precioUnitario
    if maxPesos == precioUnitario:
        maxNroFactura = nroFactura

    if cantidadArticulo < minCantArt:
        minCantArt = cantidadArticulo
    if minCantArt == cantidadArticulo:
        minCodArt = codArticulo

    if codArticulo == 1:
        totalFinalFactura1 = precioUnitario * acumTotal / 100
    if codArticulo == 3:
        totalFinalFactura3 = precioUnitario * acumTotal / 100
    if codArticulo == 5:
        totalFinalFactura5 = precioUnitario * acumTotal / 100
    if codArticulo == 7:
        totalFinalFactura7 = precioUnitario * acumTotal / 100

    nroFactura = int(input("Ingresar numero de factura: "))
    if nroFactura != 0:
        codArticulo = int(input("Ingresar codigo de articulo entre 1, 3, 5 o 7: "))
        cantidadArticulo = int(input("Ingresar cantidad del articulo: "))
        precioUnitario = int(input("Ingresar precio unitario: "))

print("Total general facturado: $", acumTotal)
print("Cantidad vendida en unidades: art.1: ", acumArt1, "unidades. Art.3: ", acumArt3, "unidades. Art.4: ",
    acumArt5, "unidades. Art.7: ", acumArt7, "unidades")
print("Total de artículos vendidos: ", sumaArt, "unidades")
print("Cantidad de facturas emitidas para cada uno de los artículos: art.1:",cont1, "art.3:", cont3, "art.5:",
      cont5, "art.7:", cont7)
print("Nro. de factura con mayor valor ( en $ ):", maxNroFactura)
print("Nro. de artículo con menor cantidad pedida:", minCodArt)
print("Porcentaje de ventas (en pesos) de cada uno de los artículos sobre el total: art.1:", totalFinalFactura1,
      "%. art.3:", totalFinalFactura3, "%. art.5:", totalFinalFactura5, "%. art.7:", totalFinalFactura7, "%")