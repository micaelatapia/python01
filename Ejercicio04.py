"""4. Se realiza un censo en la provincia de Buenos Aires. Por cada persona censada se
ingresa sexo (1.F, 2.M), edad y estudios cursados (1 para estudios primarios, 2 para
estudios secundarios ó 3 para estudios terciarios).
Diseñar un programa que permita ingresar los datos y calcular:
    a) Cantidad de hombres mayores a 45 años.
    b) Cantidad de mujeres encuestadas.
    c) Promedio de edad de las personas para cada tipo de estudio.
 ) Porcentaje de mujeres con estudios terciarios.
e) Porcentaje de hombres mayores a 30 años con estudios terciarios.
f) Promedio de edad de las mujeres mayores a 40 años con estudios secundarios."""

cont_45 = 0
cont_Mujeres = 0
acum_primaria = 0
cont_primaria = 0
acum_secundaria = 0
cont_secundaria = 0
acum_tersario = 0
cont_tersario = 0
contMujeresTer = 0

sexo = int(input("Ingresar sexo, 1.F o 2.M: "))
edad = int(input("Ingresar edad: "))
estudios = int(input("Estudios 1.primarios 2.secundarios o 3.terciaros: "))

while edad != 0 and estudios != 0:
    if sexo == 2 and edad > 45:
        cont_45 = cont_45 + 1

    if sexo == 1:
        cont_Mujeres = cont_Mujeres + 1

    if estudios == 1:
        cont_primaria = cont_primaria + 1
        acum_primaria = acum_primaria + edad

    if estudios == 2:
        cont_secundaria = cont_secundaria + 1
        acum_secundaria = acum_secundaria + edad

    if estudios == 3:
        cont_tersario = cont_tersario + 1
        acum_tersario = acum_tersario + edad

    if sexo == 1:
        if estudios == 3:
            contMujeresTer = contMujeresTer + 1

    sexo = int(input("Ingresar sexo, 1.F o 2.M: "))
    edad = int(input("Ingresar edad: "))
    estudios = int(input("Estudios 1.primarios 2.secundarios o 3.terciaros: "))

print("Cantidad de hombres mayores a 45 años:", cont_45)
print("Cantidad de mujeres encuestadas:", cont_Mujeres)
print("Promedio de estudio primario:", acum_primaria / cont_primaria, "%")
print("Promedio de secundario:", acum_secundaria / cont_secundaria, "%")
print("Promedio de estudios terciarios:", acum_tersario / cont_tersario, "%")
print("Porcentaje de mujeres con estudios terciarios:", contMujeresTer / cont_Mujeres * 100, "%")
print("Porcentaje de hombres mayores a 30 años con estudios terciarios.")