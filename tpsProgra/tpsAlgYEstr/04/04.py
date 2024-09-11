'''
Nombre: Rocco Moresi
Nombre problema:    RELOJ

Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Desarrollar un programa que pida un valor de hora, un valor de minuto, y un valor de segundo. A partir de esos valores
mostrar un reloj digital en formato de display HH:MM:SS (cada valor siempre en 2 dígitos). El display deberá avanzar cada
1 segundo como cualquier reloj digital (es decir que cuando los segundos superen los 59 volverán a 00 y se agregará un
minuto, etc. Y lo mismo entre los minutos y las horas)


Fecha: 09/07/2024

MODULOS:
'''
import time

def formato_hora(hora, minuto, segundo):
    return f"{hora:02}:{minuto:02}:{segundo:02}"

def incremento_reloj(hora, minuto, segundo):
    segundo += 1
    if segundo == 60:
        segundo = 0
        minuto += 1
    if minuto == 60:
        minuto = 0
        hora += 1
    if hora == 24:
        hora = 0
    return hora, minuto, segundo

def reloj_digital():
    hora = int(input("Introduce la hora (0-23): "))
    minuto = int(input("Introduce los minutos (0-59): "))
    segundo = int(input("Introduce los segundos (0-59): "))

    while True:
        print(formato_hora(hora, minuto, segundo), end="\r")
        time.sleep(1)
        hora, minuto, segundo = incremento_reloj(hora, minuto, segundo)

reloj_digital()

