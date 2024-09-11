'''
Nombre: Rocco Moresi
Nombre problema:REGISTRO DE PRECIPITACIONES
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:
Escribir un programa que permita grabar un archivo los datos de lluvia caída durante un año. Cada línea del archivo se
grabará con el siguiente formato:
día;mes;lluvia_caída_en_mm por ejemplo 25;5;88
El dato de la cantidad de mm caídos se generará mediante números al azar entre 0 y 100. Para el día y el mes, preguntar
al usuario por un año, y luego iniciar la registración de las precipitaciones comenzando desde el 1° de enero de dicho año,
y avanzando de a un día hasta llegar al 31/12 (Importar y usar para esto la función diaSiguiente() del módulo generado en
el ejercicio 7). Por último, se solicita leer el archivo generado e imprimir un informe en formato matricial donde cada
columna represente a un mes y cada fila corresponda a los días del mes. Imprimir además el total de lluvia caída en todo
el año.

MODULOS:
'''
import random

def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def dia_siguiente(dia, mes, anio):
    dias_en_mes = [31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dia += 1
    if dia > dias_en_mes[mes - 1]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return dia, mes, anio

def registrar_lluvias(anio):
    archivo = open("datosDeLluvia.txt", "w", encoding="utf-8")
    dia, mes = 1, 1
    while mes <= 12:
        mm = random.randint(0, 100)
        archivo.write(f"{dia};{mes};{mm}\n")
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    archivo.close()

def leer_lluvias():
    matriz_lluvias = [[0] * 12 for _ in range(31)]
    total_anual = 0

    archivo = open("datosDeLluvia.txt", "r", encoding="utf-8")
    for linea in archivo:
        dia, mes, mm = map(int, linea.strip().split(";"))
        matriz_lluvias[dia - 1][mes - 1] = mm
        total_anual += mm
    archivo.close()

    return matriz_lluvias, total_anual

def imprimir_informe(matriz_lluvias, total_anual):
    print("Informe de lluvias:")
    print("Día/Mes".ljust(10) + "".join(f"{i + 1}".rjust(8) for i in range(12)))
    for dia in range(31):
        print(str(dia + 1).ljust(10) + "".join(f"{matriz_lluvias[dia][mes]:>8}" for mes in range(12)))
    print(f"\nTotal anual de lluvia caída: {total_anual} mm")

# Solicitar el año al usuario y registrar las lluvias
anio = int(input("Ingrese el año para registrar las lluvias: "))
registrar_lluvias(anio)

# Leer el archivo y generar el informe
matriz_lluvias, total_anual = leer_lluvias()
imprimir_informe(matriz_lluvias, total_anual)
