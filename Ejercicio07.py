"""7. Una empresa de mudanzas tiene 3 camiones. Cuando una persona contrata
servicio, se lleva la boleta interna, con los siguientes datos:
 Nro. de viaje
 Nro. de camión
 Horas trabajadas
 Destino (capital o interior)
Cada camión tiene una tarifa de hora fija, que es la siguiente:
o Camión 1  :  150$
o Camión 2  :  200$
o Camión 3  :  300$
Diseñar un programa que permita ingresar los datos de cada viaje y calcular:
a) Total recaudado
    b) Cantidad de viajes realizados
    c) Cantidad de viajes de cada camión
    d) Cantidad de horas trabajadas de cada camión
    e) Cuántos viajes se hicieron al interior
El ingreso de datos finaliza con Nro. de viaje = 0 """

acumRecaudado = 0
contViajes = 0
contCamion1 = 0
contCamion2 = 0
contCamion3 = 0
acumCamion1 = 0
acumCamion2 = 0
acumCamion3 = 0
contInterior = 0

nroViaje = int(input("Ingresar numero de viaje: "))
nroCamion = int(input("Ingresar numero de camion 1, 2 o 3: "))
horasTrabajadas = int(input("Ingresar horas trabajadas: "))
destino = int(input("Ingresar destino, 1.capital o 2.interior: "))

valor1 = horasTrabajadas * 150
valor2 = horasTrabajadas * 200
valor3 = horasTrabajadas * 300

while nroViaje != 0:
    acumRecaudado = acumRecaudado + horasTrabajadas
    if nroCamion == 1:
        valor1 = horasTrabajadas * 150
        if nroCamion == 1:
            contCamion1 = contCamion1 + 1
            if nroCamion == 1:
                acumCamion1 = acumCamion1 + horasTrabajadas

    if nroCamion == 2:
        valor2 = horasTrabajadas * 200
        if nroCamion == 2:
            contCamion2 = contCamion2 + 1
            if nroCamion == 2:
                acumCamion2 = acumCamion2 + horasTrabajadas

    if nroCamion == 3:
        valor3 = horasTrabajadas * 300
        if nroCamion == 3:
            contCamion3 = contCamion3 + 1
            if nroCamion == 3:
                acumCamion3 = acumCamion3 + horasTrabajadas

    if nroViaje == nroViaje:
        contViajes = contViajes + 1
    if destino == 2:
        contInterior = contInterior + 1

    nroViaje = int(input("Ingresar numero de viaje: "))
    if nroViaje != 0:
        nroCamion = int(input("Ingresar numero de camion 1, 2, O 3: "))
        horasTrabajadas = int(input("Ingresar horas trabajadas: "))
        destino = int(input("Ingresar destino, 1.capital o 2.interior: "))

print("Cantidad de viajes del camión 1: ", contCamion1)
print("Cantidad de horas trabajadas del camion 1: ", acumCamion1)
print("Total recaudado del camion 1: $", valor1)
print("Cantidad de viajes del camión 2: ", contCamion2)
print("Cantidad de horas trabajadas del camion 2: ", acumCamion2)
print("Total recaudado del camion 2: $", valor2)
print("Cantidad de viajes del camión 3: ", contCamion3)
print("Cantidad de horas trabajadas del camion 3: ", acumCamion3)
print("Total recaudado del camion 3: $", valor3)
print("Total recaudado de todos los camiones: $", valor1 + valor2 + valor3)
print("Cantidad de viajes realizados: ", contViajes)
print("Se hicieron", contInterior, "viaje/s al interior")
