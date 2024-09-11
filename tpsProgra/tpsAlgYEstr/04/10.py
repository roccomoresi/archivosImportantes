'''
Nombre: Rocco Moresi
Nombre problema: PALABRAS DE FRASE ORDENADAS


Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Escribir una función que reciba como parámetro una cadena de caracteres en la que las palabras se encuentran separadas
por uno o más espacios. Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre
cada una.





Fecha: 09/07/2024

MODULOS:
'''

def ordenar_palabras(cadena):
    palabras = cadena.split()
    palabras_ordenadas = sorted(palabras)
    return ' '.join(palabras_ordenadas)
