'''
Nombre: Rocco Moresi
Nombre problema: DÍGITOS DE UN ENTERO
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Escribir una función que devuelva la cantidad de dígitos de un número entero, sin utilizar cadenas de caracteres.

Fecha: 21/06/2024

MODULOS:
'''



def contar_digitos(numero):
    if abs(numero) < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

# Pruebas
numero = 123456
print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")

numero = -987654321
print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")

numero = 7
print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")

numero = -3
print(f"El número {numero} tiene {contar_digitos(numero)} dígitos.")
