"""10. En una librería se venden tres tipos de artículos:
1. libros
2. artículos de escritorio
3. juguetes
De cada artículo se conocen los siguientes datos:
 tipo de artículo
 precio unitario
 nombre del artículo
 cantidad en stock de cada uno

Desarrollar un programa que permita ingresar los artículos en
existencia con los correspondientes datos, finalizando la entrada de los
mismos con un precio igual a cero (0). Además, deberá calcular:
a) la cantidad de artículos que hay de cada tipo
b) cuál es el nombre del juguete más barato
c) cuánto dinero hay invertido en la librería
(Inversión = ∑ cantidad * precio unitario) """

acumArt1 = 0
acumArt2 = 0
acumArt3 = 0
acumPrecio = 0

tipoDeArt = int(input("Ingresar tipo de articulo: "))
precioUnitario = int(input("Ingresar precio unitario: "))
nombreArt = input("Ingresar nombre del articulo: ")
cantidadStock = int(input("Ingresar cantidad de stock: "))
minimo = precioUnitario

while precioUnitario != 0:
    if tipoDeArt == 1:
        acumArt1 = acumArt1 + tipoDeArt
    if tipoDeArt == 2:
        acumArt2 = acumArt2 + tipoDeArt
    if tipoDeArt == 3:
        acumArt3 = acumArt3 + tipoDeArt
    if nombreArt == nombreArt:
        if precioUnitario < minimo:
            minimo = precioUnitario
            print("Juguete mas barato: ", nombreArt)

    inversion = cantidadStock * precioUnitario
    tipoDeArt = int(input("Ingresar tipo de articulo: "))
    precioUnitario = int(input("Ingresar precio unitario: "))
    nombreArt = input("Ingresar nombre del articulo: ")
    cantidadStock = int(input("Ingresar cantidad de stock: "))


print("La cantidad de art de cada tipo: ", acumArt1, acumArt2, acumArt3)
print("Dinero invertido: $", inversion)