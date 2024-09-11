'''
Nombre: Rocco Moresi
Nombre problema:  TABLA DE N
Materia: algoritmos y estructuras de datos 1
LU: 1185425

Descripcion: 
Escribir una función que reciba un número entero N y devuelva un diccionario por comprensión con la tabla de multiplicar
de N del 1 al 12. Mostrar la tabla de multiplicar con el formato apropiado


Fecha: 27/06/2024

MODULOS:
'''


def devuelveMult(n):
    diccionario = {}
    num = 1
    
    for i in range(1,13,1):
        diccionario[i] = n
        num+=1
    
        
    return diccionario

n = 5
f = devuelveMult(n)
for e in f:
    print(f"{e*f[e]}")




