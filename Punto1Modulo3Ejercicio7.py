num1 = int(input("Ingresar un numero: "))
num2 = int(input("Ingresar otro numero: "))

print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("5.Salir")

opcion = int(input("Selecciones una opcion: "))

if num2 == 0:
    print("Error, no se puede dividir por 0")
    num1 = int(input("Ingresar un numero"))
    num2 = int(input("Ingresar otro numero"))

while opcion > 5 or opcion <= 0:
    print("Error")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
    opcion = int(input("Selecciones una opcion correcta: "))

while opcion < 5 and opcion > 0:
    if opcion == 1:
        print("El resultado de la suma es:", num1 + num2)
    if opcion == 2:
        print("El resultado de la resta es:", num1 - num2)
    if opcion == 3:
        print("El resultado de la multiplicación es:", num1 * num2)
    if opcion == 4:
        print("El resultado de la división es:", num1 / num2)

    num1 = int(input("Ingresar un numero: "))
    num2 = int(input("Ingresar otro numero: "))

    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Salir")
