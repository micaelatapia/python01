"""17. Ingresar las medidas de dos ángulos expresados en grados minutos y
segundos y hallar la suma. (recordar que los minutos y los segundos no deben
excederse de 60)"""


AnguloGrados = int(input("Ingresar medida de un angulo en grados: "))
AnguloMinutos = int(input("Ingresar medida de un angulo en minutos: "))
AnguloSegundos = int(input("Ingresar medida de un angulo en segundos: "))

AnguloGrados2 = int(input("Ingresar medida de otro angulo en grados: "))
AnguloMinutos2 = int(input("Ingresar medida de otro angulo en minutos: "))
AnguloSegundos2 = int(input("Ingresar medida de otro angulo en segundos: "))

SumaGrados = AnguloGrados + AnguloGrados2
SumaMinutos = AnguloMinutos + AnguloMinutos2
SumaSegundos = AnguloSegundos + AnguloSegundos2

if SumaSegundos >= 60:
    restante = SumaSegundos - 60
    SumaMinutos = SumaMinutos + restante
    print("Los segundos son: ", restante)
    if SumaSegundos >= 60:
        restante = SumaSegundos - 60
        SumaMinutos = SumaMinutos + restante
        print("Los segundos son: ", restante)