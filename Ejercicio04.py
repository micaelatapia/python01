cont_45 = 0
cont_Mujeres = 0
acum_primaria = 0
cont_primaria = 0
acum_secundaria = 0
cont_secundaria = 0
acum_tersario = 0
cont_tersario = 0
cont_MujeresTer = 0

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
        cont_MujeresTer = cont_MujeresTer + 1
        resta = cont_Mujeres - cont_MujeresTer
        porcentaje = resta * cont_Mujeres / 100
    sexo = int(input("Ingresar sexo, 1.F o 2.M: "))
    edad = int(input("Ingresar edad: "))
    estudios = int(input("Estudios 1.primarios 2.secundarios o 3.terciaros: "))
print("la cantidad de hombres mayores a 45 es: ", cont_45)
print("la cantidad de mujeres encuestadas es de: ", cont_Mujeres)
print("el promedio de estudio primario es de: ", acum_primaria / cont_primaria, "%")
print("el promedio de secundario es de: ", acum_secundaria / cont_secundaria, "%")
print("el promedio de estudio tersario es de: ", acum_tersario / cont_tersario, "%")
print("el porcentaje de mujeres con estudio terciario es de: ", porcentaje, "%")
