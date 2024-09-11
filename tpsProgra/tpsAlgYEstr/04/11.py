'''
Nombre: Rocco Moresi
Nombre problema:  REEMPLAZO DE PALABRA


Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Desarrollar una función para reemplazar todas las apariciones de una palabra por otra en una cadena de caracteres y
devolver la cadena obtenida y un entero con la cantidad de reemplazos realizados. Tener en cuenta que sólo deben
reemplazarse palabras completas, y no fragmentos de palabras. Escribir también un programa para verificar el
comportamiento de la función.




Fecha: 09/07/2024

MODULOS:
'''

def reemplazar_palabra(cadena, palabra_buscar, palabra_reemplazar):
    palabras = cadena.split()
    contador_reemplazos = 0
    
    for i in range(len(palabras)):
        if palabras[i] == palabra_buscar:
            palabras[i] = palabra_reemplazar
            contador_reemplazos += 1
    
    cadena_actualizada = ' '.join(palabras)
    return cadena_actualizada, contador_reemplazos


cadena_original = "La casa es grande y la casa es bonita."
palabra_buscar = "casa"
palabra_reemplazar = "hogar"

cadena_nueva, cantidad_reemplazos = reemplazar_palabra(cadena_original, palabra_buscar, palabra_reemplazar)
print(f"Cadena original: {cadena_original}")
print(f"Cadena con reemplazos: {cadena_nueva}")
print(f"Cantidad de reemplazos realizados: {cantidad_reemplazos}")
