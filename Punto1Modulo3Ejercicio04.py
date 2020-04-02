cont = 0

contp = 0
acump = 0

conta = 0
acuma = 0







may = ausentes
Escribir
"Cursos (1-5)"
cont = cont + 1
Para
cont
Desde
1
Hasta
5
Con
Paso
1
Escribir
cont
FinPara

Escribir
"Ingresar en orden de curso la cantidad de presentes"
p = presentes
Mientras
contp < 5
contp = contp + 1
acump = acump + p
Leer
p
Mientras
p < 1
Escribir
"Error, ingresar numero correcto"
Leer
p
FinMientras

FinMientras

Escribir
"Ingresar en orden de curso la cantidad de ausentes"
a = ausentes
Mientras
conta < 5
conta = conta + 1
acuma = acuma + a
Leer
a
Mientras
a < 0
Escribir
"Error, ingresar numero correcto"
Leer
a
FinMientras
resta = (p - a)
porcentaje = resta / p * 100
Escribir
" el porcentaje de presencia del curso es de ", porcentaje
"%"

Si
ausentes > may
Entonces
may = ausentes
cursomayor =
FinSi

FinMientras

cont = p
Escribir
"Los ausentes son: ", acuma + a
Escribir
"El curso con mayor ausente es: ", curso