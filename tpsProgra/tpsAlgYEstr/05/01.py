'''
Nombre: Rocco Moresi
Nombre problema:  CADENAS A REALES CON MANEJADOR DE EXCEPCIONES



Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion: Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales, sume ambos
valores y devuelva el resultado como un número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.

Fecha: 09/07/2024

MODULOS:
'''

def manejDeEx(cadena1, cadena2):
    try:
        res = int(cadena1) + int(cadena2)
        return res
    except ValueError:
        print("Valor erroneo")
        


cadena1 = input("")
cadena2 = input("")

f = manejDeEx(cadena1, cadena2)
if f != None:
    print(f)

