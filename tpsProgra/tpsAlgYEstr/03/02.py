'''
Nombre: Rocco Moresi
Nombre problema: GENERACION DE MATRICES CON PATRONES
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Escribir un programa con un menú que invoque a cada una de ellas y muestre por pantalla la matriz obtenida. El tamaño 
de las matrices debe establecerse como N x N solicitando el valor por teclado, y las funciones deben servir para cualquier 
valor ingresado. Antes de volver al menú detener el programa y continuar con ENTER. 

Fecha: 21/06/2024

MODULOS:
'''
import math

def generarMatriz(n):
    matriz = []
    for j in range(n):
        fila = []
        for i in range(n):
            fila.append(0)
        matriz.append(fila)
    return matriz

def generarMatrizA(matriz,n):
    matriz = []
    flag = 0
    num = 1
    for j in range(n):
        fila = []
        for i in range(n):
            if i == flag:
                fila.append(num)
                num+=2
            else:
                fila.append(0)
        flag+=1
        
        matriz.append(fila)
    return matriz

def generarMatrizB(matriz,n):
    matriz = []
    flag = n - 1
    num = 27
    for j in range(n):
        fila = []
        for i in range(n):
            if i == flag:
                fila.append(num)
            else:
                fila.append(0)
        matriz.append(fila)
        num/=3
        flag-=1
        
    return matriz



#PROGRAMA PRINCIPAL

tamañoDeMatriz = int(input("Ingrese el tamañano de matriz que desea: ")) 

mat = input("Ingresar matriz que desea mostrar: ")

matriz = []



if mat == "a":
    matrizA = generarMatrizA(matriz,tamañoDeMatriz)
    for e in matrizA:
        print(e)

elif mat == "b":
    matrizB = generarMatrizB(matriz,tamañoDeMatriz)
    for y in matrizB:
        print(y)