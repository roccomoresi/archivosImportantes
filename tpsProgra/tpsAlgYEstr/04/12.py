'''
Nombre: Rocco Moresi
Nombre problema:  VOCALES ARRIBA


Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Se está desarrollando una importante app para tratamiento de texto y nos piden que desarrollemos una función para una
de las opciones de la app. La función consiste en poner en mayúscula todas las vocales de una frase, por ejemplo, si la
función recibe el texto “frase de prueba para el nuevo programa de tratamiento de texto” debe devolver “frAsE dE prUEbA
pArA El nUEvO prOgrAmA dE trAtAmIEntO dE tExtO”. Probar la función desde un programa principal





Fecha: 09/07/2024

MODULOS:
'''

def convertir_vocales_mayusculas(frase):
    vocales = 'aeiou'
    resultado = []
    
    for letra in frase:
        if letra.lower() in vocales:
            resultado.append(letra.upper())
        else:
            resultado.append(letra)
    
    return ''.join(resultado)


if __name__ == "__main__":
    texto = "frase de prueba para el nuevo programa de tratamiento de texto"
    resultado = convertir_vocales_mayusculas(texto)
    print("Texto original:", texto)
    print("Texto con vocales en mayúsculas:", resultado)
