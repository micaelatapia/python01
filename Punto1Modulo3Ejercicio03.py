cont = 0

num = int(input("Ingrese numero: "))

while num != 0:
    if num > 0:
        cont = cont + 1
    num = int(input("Ingrese numero: "))

print("Cantidad de numeros positivos ingresados: ", cont)
