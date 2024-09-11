'''
Nombre: Rocco Moresi
Nombre problema: PUNTO CADA 3 DÍGITOS


Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion: Escribir una función que reciba una cadena que contiene un número entero de muchos dígitos y devuelva una cadena con
el mismo número, pero con los puntos de las separaciones de miles. Por ejemplo, si recibe 1234567890, debe devolver
1.234.567.890



Fecha: 09/07/2024

MODULOS:
'''

def formatear_con_puntos(numero):
    num_entero = int(numero)
    numero_formateado = f"{num_entero:,}".replace(",", ".")
    return numero_formateado

numero = "1234567890"
resultado = formatear_con_puntos(numero)
print(resultado)  

numero = "987654321"
resultado = formatear_con_puntos(numero)
print(resultado)  

numero = "1000"
resultado = formatear_con_puntos(numero)
print(resultado)  
