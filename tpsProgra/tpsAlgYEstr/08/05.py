'''
Nombre: Rocco Moresi
Nombre problema:    PALABRAS ÚNICAS
Materia: algoritmos y estructuras de datos 1
LU: 1185425

Descripcion: Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de
cada una. Finalmente mostrar las palabras ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso




Fecha: 27/06/2024

MODULOS:
'''

frase = input("Ingresa frase: ")


fraseLista = frase.split(" ")

fraseConjunto = set(fraseLista)



x = sorted(fraseConjunto,key=len)


print(x)
