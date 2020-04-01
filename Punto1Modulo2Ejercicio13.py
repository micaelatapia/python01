"""13. El usuario deberá pensar en uno de los siguientes personajes: LIO
MESSI, MAURICIO MACRI y MIRTHA LEGRAND. El programa mediante
algunas preguntas convenientes (edad, sexo, ocupación, etc) deberá mostrar
de que personaje se trata. Ejemplo: si es hombre y deportista tendrá que decir
Lio Messi"""

edades = int(input("Ingresar edades: "))
sexo = int(input("Ingresar sexo: "))
ocupacion = int(input("Ingresar ocupacion: "))

masculino = int(input(sexo))
futbolista = int(input(ocupacion))
presidente = int(input(ocupacion))
femenino = int(input(sexo))
conductora = int(input(ocupacion))

if edades == 30 and sexo == masculino and ocupacion == futbolista:
    print("Lionel Messi")
if edades == 70 and sexo == masculino and ocupacion == presidente:
    print("Macri")
if edades == 92 and sexo == femenino and ocupacion == conductora:
    print("Mirtha Legrand")