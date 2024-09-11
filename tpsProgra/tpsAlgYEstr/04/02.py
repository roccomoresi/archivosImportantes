'''
Nombre: Rocco Moresi
Nombre problema:  TEXTO CENTRADO EN PANTALLA
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:
Leer una cadena de caracteres e imprimirla centrada rellenando a izquierda y derecha con guiones para cubrir toda la
pantalla. Suponer que la pantalla tiene 80 columnas. En el mismo programa hacer 3 versiones: una sin utilizar facilidades
de Python, otra usando la facilidad de función o método incorporado, y otra usando la facilidad de f-strings.
Fecha: 09/07/2024

MODULOS:
'''

def centrar_sin_facilidades(cadena):
    longitud_cadena = len(cadena)
    longitud_total = 80
    longitud_relleno = longitud_total - longitud_cadena
    longitud_relleno_izq = longitud_relleno // 2
    longitud_relleno_der = longitud_relleno - longitud_relleno_izq
    cadena_centrada = '-' * longitud_relleno_izq + cadena + '-' * longitud_relleno_der
    print(cadena_centrada)



def centrar_con_metodo(cadena):
    cadena_centrada = cadena.center(80, '-')
    print(cadena_centrada)

def centrar_con_fstrings(cadena):
    longitud_total = 80
    longitud_relleno_izq = (longitud_total - len(cadena)) // 2
    longitud_relleno_der = longitud_total - len(cadena) - longitud_relleno_izq
    cadena_centrada = f"{'-' * longitud_relleno_izq}{cadena}{'-' * longitud_relleno_der}"
    print(cadena_centrada)


cadena = input("Introduce una cadena: ")
centrar_con_metodo(cadena)


cadena = input("Introduce una cadena: ")
centrar_sin_facilidades(cadena)


cadena = input("Introduce una cadena: ")
centrar_con_fstrings(cadena)