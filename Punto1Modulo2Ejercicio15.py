"""15. Ingresar la medida de un ángulo y determinar si es agudo, obtuso, recto,
nulo o llano. Si el valor ingresado es mayor a 180º mostrar la leyenda “ángulo
no válido” e ingresar un nuevo valor"""


Angulo = int(input("Ingresar medida de un angulo: "))

while Angulo < 90 and Angulo > 0:
    print("angulo agudo")

while Angulo == 90:
    print("angulo recto")

while Angulo > 90 and Angulo < 180:
    print("angulo obtuso")

while Angulo == 180:
    print("angulo llano")

while Angulo > 180 or Angulo <= 0:
    print("Ángulo no valido")
    Angulo = int(input("Ingresar medida de otro angulo: "))
