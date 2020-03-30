"""9. Un negocio vende empanadas y hace entregas a domicilio.
Los datos que recibe el sistema son:
 dirección cliente
 cantidad de empanadas
 tipo de empanadas. 1. horno; 2. frita; 3. dulce.
Las empanadas al horno cuestan $18 cada una, las fritas $19,
y las dulces (de membrillo o batata) $21
La entrada de datos termina con cantidad de empanadas = 0
El sistema debería mostrar:
 a) Dirección del cliente que más empanadas compró.
 b) Cantidad de empanadas vendidas de cada tipo.
 c) Mostrar la dirección de los clientes que compraron más de 15 empanadas
de horno
 d) Total recaudado(Cada cliente pide un solo tipo de empanada)"""


acumEmpanadas = 0
acumDireccion = " "

acumHorno = 0
acumFrita = 0
acumDulce = 0

acumTotal1 = 0
acumTotal2 = 0
acumTotal3 = 0


direccion = input("Ingrese direccion del cliente: ")
cantidadEmpanadas = int(input("Cantidad de empanadas: "))
tipoEmpanada = int(input("Tipo de empanada: 1.horno 2.frita 3.dulce: "))


maximo = cantidadEmpanadas
puntoA = direccion

while cantidadEmpanadas != 0:

    if tipoEmpanada == 1 and cantidadEmpanadas > 15:
        acumDireccion = acumDireccion + " / " + direccion

    if tipoEmpanada == 1:
        acumHorno = acumHorno + cantidadEmpanadas

    if tipoEmpanada == 2:
        acumFrita = acumFrita + cantidadEmpanadas

    if tipoEmpanada == 3:
        acumDulce = acumDulce + cantidadEmpanadas

    if tipoEmpanada == 1:
        tipoEmpanada = cantidadEmpanadas * 18
        acumTotal1 = acumTotal1 + tipoEmpanada
    if tipoEmpanada == 2:
        tipoEmpanada = cantidadEmpanadas * 19
        acumTotal2 = acumTotal2 + tipoEmpanada
    if tipoEmpanada == 3:
        tipoEmpanada = cantidadEmpanadas * 21
        acumTotal3 = acumTotal3 + tipoEmpanada

    if cantidadEmpanadas > maximo:
        maximo = cantidadEmpanadas
    if maximo == cantidadEmpanadas:
        puntoA = direccion

    direccion = input("Ingrese direccion del cliente: ")
    cantidadEmpanadas = int(input("Cantidad de empanadas: "))
    tipoEmpanada = int(input("Tipo de empanada: 1.horno 2.frita 3.dulce: "))

print("Dirección del cliente que más empanadas compró: ", puntoA)

print("Cantidad de empanadas vendidas de cada tipo: horno:", acumHorno,
    "frita: ", acumFrita, "dulces: ", acumDulce)

print("La direccion de clientes que compraron mas de 15 empanadas al horno: ",
    acumDireccion)

print("Total recaudado: $", acumTotal1 + acumTotal2 + acumTotal3)