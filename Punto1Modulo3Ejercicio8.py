acum = 0
cont = 0
edad = int(input("Ingrese edad de 50 empleados: "))
max = edad
min = edad

while cont < 3:
    acum = acum + edad
    cont = cont + 1

    if edad > max:
        max = edad
    if edad < min:
        min = edad

    edad = int(input("Ingrese edad de 50 empleados: "))

print("El rango de edad es enter", min, "y", max)
