'''
Nombre: Rocco Moresi
Nombre problema: FUNCIÓN TOMAR SUBCADENA


Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion: Desarrollar una función que extraiga una subcadena de una cadena de caracteres, indicando la posición y la cantidad de
caracteres deseada. Devolver la subcadena como valor de retorno. Escribir también un programa para verificar el
comportamiento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que
comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena "4356-7890". Escribir una función para cada uno
de los siguientes casos:
A. Utilizando rebanadas
B. Sin utilizar rebanadas



Fecha: 09/07/2024

MODULOS:
'''

def extraer_subcadena_con_rebanadas(cadena, inicio, cantidad):
    subcadena = cadena[inicio:inicio + cantidad]
    return subcadena

def extraer_subcadena_sin_rebanadas(cadena, inicio, cantidad):
    subcadena = ""
    for i in range(inicio, inicio + cantidad):
        subcadena += cadena[i]
    return subcadena


cadena = "El número de teléfono es 4356-7890"
inicio = 25
cantidad = 9
resultado = extraer_subcadena_sin_rebanadas(cadena, inicio, cantidad)
print(resultado)  



cadena = "El número de teléfono es 4356-7890"
inicio = 25
cantidad = 9
resultado = extraer_subcadena_con_rebanadas(cadena, inicio, cantidad)
print(resultado)  
