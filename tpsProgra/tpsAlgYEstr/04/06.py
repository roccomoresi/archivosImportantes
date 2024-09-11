'''
Nombre: Rocco Moresi
Nombre problema: FILTRADO DE PALABRAS

Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:



Fecha: 09/07/2024

MODULOS:
'''

def filtrarPalabrasA(frase, n):
    palabras = []
    palabra = ""
    
    for char in frase:
        if char == " ":
            if len(palabra) >= n:
                palabras.append(palabra)
            palabra = ""
        else:
            palabra += char
            
    if len(palabra) >= n:
        palabras.append(palabra)
    
    return " ".join(palabras)

def filtrarPalabrasB(frase, n):
    palabras = frase.split()
    resultado = []
    
    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
    
    return " ".join(resultado)

def filtrarPalabrasC(frase, n):
    palabras = frase.split()
    resultado = [palabra for palabra in palabras if len(palabra) >= n]
    return " ".join(resultado)


frase = "hola a mi me gusta la saga de crepusculo"
N = 4
resultado = filtrarPalabrasC(frase, N)
print(resultado)  














frase = "hola a mi me gusta la saga de crepusculo"
N = 4
resultado = filtrarPalabrasB(frase, N)
print(resultado)










frase = "hola a mi me gusta la saga de crepusculo"
N = 4
resultado = filtrarPalabrasA(frase, N)
print(resultado)
