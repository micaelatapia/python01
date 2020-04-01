"""Calcular los kilómetros recorridos por un automóvil conociendo el
kilometraje inicial y el actual. Mostrar una leyenda según la distancia recorrida:
Para 100 Km. o menos: “Paciencia, falta mucho”
Más de 100 Km. y menos de 200: “Parar para desayunar”
Más de 200 Km.: “Se recomienda cargar combustible”"""

KilometrajeInicial = int(input("Agregar kilometraje inicial: "))
KilometrajeActual = int(input("Agregar kilometraje actual: "))

resultado = KilometrajeInicial - KilometrajeActual

if resultado <= 100 and resultado > 0:
    print("Paciencia, falta mucho")

if resultado > 100 and resultado < 200:
    print("Parar para desayunar")

if resultado >= 200:
    print("Se recomienda cargar combustible")

if resultado < 0:
    print("Ya supero su recorrido")