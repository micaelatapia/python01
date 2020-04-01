"""10. Calcular el importe que debe pagar un auto en un estacionamiento
teniendo en cuenta como datos las horas y minutos de uso. El valor de la hora
es de $45 y si los minutos exceden de 15 se incrementa una hora al importe. El
mínimo a cobrar es de una hora"""

CantidadDeHoras = int(input("Ingrese cantidad de horas: "))
CantidadDeMinutos = int(input("Ingresar cantidad de minutos: "))

if CantidadDeMinutos >= 15:
    CantidadDeHoras = CantidadDeHoras + 1

print ("El valor es de: $", CantidadDeHoras * 45)