'''
Nombre: Rocco Moresi
Nombre problema:FUNCIÓN ELIMINAR SUBCADENA


Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de
caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la
misma. Escribir una función para cada uno de los siguientes casos:
A. Utilizando rebanadas
B. Sin utilizar rebanadas




Fecha: 09/07/2024

MODULOS:
'''

def eliminar_subcadena_con_rebanadas(cadena, inicio, cantidad):
    parte1 = cadena[:inicio]
    parte2 = cadena[inicio + cantidad:]
    return parte1 + parte2

def eliminar_subcadena_sin_rebanadas(cadena, inicio, cantidad):
    nueva_cadena = ""
    for i, char in enumerate(cadena):
        if i < inicio or i >= inicio + cantidad:
            nueva_cadena += char
    return nueva_cadena

cadena = "El número de teléfono es 4356-7890"
inicio = 25
cantidad = 9
resultado = eliminar_subcadena_sin_rebanadas(cadena, inicio, cantidad)
print(resultado)  # Output esperado: "El número de teléfono es "


cadena = "El número de teléfono es 4356-7890"
inicio = 25
cantidad = 9
resultado = eliminar_subcadena_con_rebanadas(cadena, inicio, cantidad)
print(resultado)  
