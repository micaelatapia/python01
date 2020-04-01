GananciaAnual = int(input("Ingresar ganancia anual: "))

if GananciaAnual <= 10000:
    print("La retencion es de 0 (cero)")

if GananciaAnual > 10000 and GananciaAnual <= 15000:
    print("La retencion es de: ", (GananciaAnual - 10000) * 2 / 100)

if GananciaAnual > 15000:
    print("La retencion es de: ", (GananciaAnual - 15000) * 5 / 100)