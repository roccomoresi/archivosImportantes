'''Nombre: Rocco Moresi
Nombre problema: BINARIO A DECIMAL
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Desarrollar una función que reciba un número binario y lo devuelva convertido a base decimal.
Fecha: 24/06/2024
MODULOS:
'''

def binario_a_decimal(binario):
    if len(binario) == 1:
        return int(binario)
    else:
        return int(binario[-1]) + 2 * binario_a_decimal(binario[:-1])

binario = "1101"
print(f"El número binario {binario} en decimal es {binario_a_decimal(binario)}.")

binario = "10101"
print(f"El número binario {binario} en decimal es {binario_a_decimal(binario)}.")

binario = "11111111"
print(f"El número binario {binario} en decimal es {binario_a_decimal(binario)}.")

    
