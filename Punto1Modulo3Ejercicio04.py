"""4) Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo
de cada curso:
 Curso (1-5)
 Presentes
 Ausentes
Calcular
 Por cada curso el porcentaje de presentes sobre el total
 Cantidad de ausentes en el colegio
 Curso con mayor cantidad de ausente"""

ausentes = 0
contA = 0
acumA = 0

curso1 = print("Curso 1")
curso2 = print("Curso 2")
curso3 = print("Curso 3")
curso4 = print("Curso 4")
curso5 = print("Curso 5")


print("Ingresar presentes de cada curso:")
curso1p = int(input("Curso 1: "))
curso2p = int(input("Curso 2: "))
curso3p = int(input("Curso 3: "))
curso4p = int(input("Curso 4: "))
curso5p = int(input("Curso 5: "))
totalP = curso1p + curso2p + curso3p + curso4p + curso5p

while contA < 5:
    contA = contA + 1
    acumA = acumA + ausentes
    ausentes = int(input("Ingresar ausentes de cada curso: "))


print(acumA)
print("Porcentaje de presentes en el curso 1:", curso1p / (totalP + acumA) * 100)







