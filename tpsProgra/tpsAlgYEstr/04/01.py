'''
Nombre: Rocco Moresi
Nombre problema:  CADENA CAPICÚA
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas.
Escribir además un programa que permita verificar su funcionamiento.
Fecha: 09/07/2024

MODULOS:
'''

def esONoCapicua(cadena):
    for i in range(len(cadena)//2):
        if cadena[i] != cadena[-(i+1)]:
            return False
    return True



cadena = input("Es capicua? ")

c = esONoCapicua(cadena)

print(c)