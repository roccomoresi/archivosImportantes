'''
Nombre: Rocco Moresi
Nombre problema:   FICHAS DOMINÓ
Materia: algoritmos y estructuras de datos 1
LU: 1185425

Descripcion:Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas en dos tuplas, por ejemplo:
(3, 4) y (5, 4). La función devolverá True o False. Escribir también un programa para verificar su comportamiento.
Considerar el uso de conjuntos para resolver este ejercicio.



Fecha: 27/06/2024

MODULOS:
'''

def encajanLas(conjunto1,conjunto2):
    x = conjunto1 & conjunto2
    if len(x) >= 1:
        return True
    else:
        return False

dominoUno = {5,3}
dominoDos = {1,4}

c = encajanLas(dominoUno,dominoDos)

print("\n",c)