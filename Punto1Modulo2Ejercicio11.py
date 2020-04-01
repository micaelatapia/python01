"""11. Se ingresa el código de tipo de llamada: 1. Local 2. Interurbana 3.
Internacional y la duración en minutos de la misma. Si el minuto cuesta $0.25
para la llamada local, $0.40 para la llamada interurbana y $1.05 para la llamada
internacional, diseñar un algoritmo que permita calcular el monto a pagar por
dicha llamada"""

CodLlamada = int(input("Ingresar codigo de llamada 1.Local 2.Interurbana 3.Internacional"))

MinLlamada = int(input("Ingresar minutos de la llamada: "))

if CodLlamada == 1:
    print("El precio de la llamada es de: $", 0.25 * MinLlamada)

if CodLlamada == 2:
    print("El precio de la llamada es de: $", 0.40 * MinLlamada)

if CodLlamada == 3:
    print("El precio de la llamada es de: $", 1.05 * MinLlamada)