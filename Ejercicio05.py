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
  h) Porcentaje de ventas (en pesos) de cada uno de
  los artículos sobre el total.
  La entrada de datos finaliza con un número de factura igual a cero"""

cont = 0

totalFactura1 = 0


acumArt1 = 0
acumArt3 = 0
acumArt5 = 0
acumArt7 = 0

nroFactura = int(input("Ingresar numero de factura: "))
codArticulo = int(input("Ingresar codigo de articulo entre 1, 3 ,5 o 7: "))
cantidadArticulo = int(input("Ingresar cantidad del articulo: "))
precioUnitario = int(input("Ingresar precio unitario: "))

while nroFactura != 0:
    cont = cont + 1
    if nroFactura == nroFactura:
        totalFactura1 = cantidadArticulo * precioUnitario


    if codArticulo == 1:
        acumArt1 = acumArt1 + cantidadArticulo
    if codArticulo == 3:
        acumArt3 = acumArt3 + cantidadArticulo
    if codArticulo == 5:
        acumArt5 = acumArt5 + cantidadArticulo
    if codArticulo == 7:
        acumArt7 = acumArt7 + cantidadArticulo




    nroFactura = int(input("Ingresar numero de factura: "))
    if nroFactura != 0:
        codArticulo = int(input("Ingresar codigo de articulo entre 1, 3 ,5 o 7: "))
        cantidadArticulo = int(input("Ingresar cantidad del articulo: "))
        precioUnitario = int(input("Ingresar precio unitario: "))

print("Total de cada factura: ", )
print("Total general facturado: ", cont)
print("Cantidad vendida en unidades es de: art.1: ", acumArt1, "unidades. Art.3: ", acumArt3, "unidades. Art.4: ",
    acumArt5, "unidades. Art.7: ", acumArt7, "unidades")