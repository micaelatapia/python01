cont = 0

temperaturas = int(input("Ingrese temperaturas: "))
max = temperaturas
min = temperaturas

while cont < 5:
    cont = cont + 1

    if temperaturas > max:
        max = temperaturas
    if temperaturas < min:
        min = temperaturas

    temperaturas = int(input("Ingrese temperaturas: "))

print("La temperatura minima es:", min, "y la maxima:", max)