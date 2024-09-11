'''
Nombre: Rocco Moresi
Nombre problema: TEMPORIZADOR

Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Desarrollar un programa que pida un valor de minuto, y un valor de segundo. A partir de esos valores mostrar un reloj
digital en formato de display MM:SS (cada valor siempre en 2 dígitos). El display deberá ir en cuenta regresiva cada 1
segundo hasta llegar a 00:00. Cuando llegue a cero deberá detenerse y mostrar el mensaje “<<<< TIEMPO >>>>”



Fecha: 09/07/2024

MODULOS:
'''

import time

def formato_tiempo(minuto, segundo):
    return f"{minuto:02}:{segundo:02}"

def cuenta_regresiva(minuto, segundo):
    while minuto > 0 or segundo > 0:
        print(formato_tiempo(minuto, segundo), end="\r")
        time.sleep(1)
        if segundo == 0:
            if minuto > 0:
                minuto -= 1
                segundo = 59
        else:
            segundo -= 1
    print(formato_tiempo(minuto, segundo))
    print("<<<< TIEMPO >>>>")

def reloj_cuenta_regresiva():
    minuto = int(input("Introduce los minutos: "))
    segundo = int(input("Introduce los segundos: "))
    cuenta_regresiva(minuto, segundo)

reloj_cuenta_regresiva()
