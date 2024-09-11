'''
Nombre: Rocco Moresi
Nombre problema:  MES NÚMERO A TEXTO CON MANEJADOR DE EXCEPCIONES

Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion: Desarrollar una función que devuelva una cadena de caracteres con el nombre del mes cuyo número se recibe como
parámetro. Los nombres de los meses deberán obtenerse de una lista de cadenas de caracteres inicializada dentro de la
función. Devolver una cadena vacía si el número de mes es inválido. La detección de meses inválidos deberá realizarse a
través de excepciones.

Fecha: 09/07/2024

MODULOS:
'''

def obtener_nombre_mes(numero_mes):
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]

    try:
        nombre_mes = meses[numero_mes - 1]
        return nombre_mes
    except IndexError:
        return ""

numeros_meses = [1, 3, 6, 12, 13, 0, -1]

for numero_mes in numeros_meses:
    nombre_mes = obtener_nombre_mes(numero_mes)
    if nombre_mes:
        print(f"Mes {numero_mes}: {nombre_mes.capitalize()}")
    else:
        print(f"Mes {numero_mes}: Mes inválido")
