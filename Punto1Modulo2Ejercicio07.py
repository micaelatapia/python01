"""7. Ingresar las edades de dos personas. Si una de ellas es mayor de edad
y la otra menor de edad, calcular y mostrar su promedio. En caso contrario
mostrar las dos edades"""

edad1 = int(input("Ingresar una edad: "))
edad2 = int(input("Ingresar otra edad: "))

if edad1 < 18 and edad2 >= 18 or edad1 >= 18 and edad2 < 18:
    print("El promedio es: ", (edad1 + edad2) / 2)
else:
    print("Las edades son: ", edad1 , " y ", edad2)