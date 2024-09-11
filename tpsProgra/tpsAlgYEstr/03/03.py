'''
Nombre: Rocco Moresi
Nombre problema: MATRIZ ALEATORIA SIN REPETICIONES
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Desarrollar un programa para rellenar una matriz de N x N con números enteros al azar comprendidos en el intervalo 
[0,N2), de tal forma que ningún número se repita. Imprimir la matriz por pantalla. 

Fecha: 21/06/2024

MODULOS:'''
import random



def generarMatriz(matriz,n):
    
    for j in range(n):
        fila = []
        for i in range(n):
            fila.append(0)
        matriz.append(fila)
    
    return matriz

def sinRepeticiones(matriz,n):
    lista = []

    for i in range(len(matriz[0])):
        aux = random.randint(1,70)
        for t in matriz:
            if t != 0:
                lista.append(t)
        while aux not in lista and len(matriz[i]) <= n:
            matriz[i].append(aux)
            aux = random.randint(1,70)    
            for t in matriz:
                if t != 0:
                    lista.append(t)

        for t in matriz:
            lista.append(t)


    return matriz

#programa principal 

n = int(input("Ingrese cantidad de numeros q desea en la matriz: "))
matriz = []

m = generarMatriz(matriz,n)
for j in m:
    print(j)

print("\n")


d = sinRepeticiones(matriz,n)
for u in d:
    print(u)





