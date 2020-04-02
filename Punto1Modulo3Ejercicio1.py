nros = int(input("Ingresar numeros hasta un multiplo de 3: "))

if nros == 0:
    nros = int(input(""))

while nros % 3 != 0:
    nros = int(input(""))

print("El ultimo numero ingresado es ", nros)