'''
Nombre: Rocco Moresi
Nombre problema: NÓMINA DE EMPLEADOS
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion: Se dispone de dos formatos diferentes de archivos de texto en los que se almacenan datos de empleados, detallados más
abajo. Desarrollar un programa para cada uno de los formatos suministrados, que permitan leer cada uno de los archivos
y grabar los datos obtenidos en otro archivo de texto con formato CSV.
Los archivos de entrada pueden ser creados mediante el Block de Notas o Notepad++. Ambos archivos tienen tres campos
por registro: Apellido y Nombre, Fecha de alta y Domicilio.
Fecha: 21/06/2024

MODULOS:
'''

import csv

def leer_formato_1(nombre_archivo_entrada, nombre_archivo_salida):
    try:
        archivo_entrada = open(nombre_archivo_entrada, "r", encoding="utf-8")
        archivo_salida = open(nombre_archivo_salida, "w", newline="", encoding="utf-8")

        writer = csv.writer(archivo_salida)
        writer.writerow(["Apellido y Nombre", "Fecha de alta", "Domicilio"])

        for linea in archivo_entrada:
            apellido_nombre = linea[0:20].strip()
            fecha_alta = linea[20:28].strip()
            domicilio = linea[28:].strip()
            writer.writerow([apellido_nombre, fecha_alta, domicilio])

    except Exception as e:
        print(f"Error: {e}")
    finally:
        archivo_entrada.close()
        archivo_salida.close()

def leer_formato_2(nombre_archivo_entrada, nombre_archivo_salida):
    try:
        archivo_entrada = open(nombre_archivo_entrada, "r", encoding="utf-8")
        archivo_salida = open(nombre_archivo_salida, "w", newline="", encoding="utf-8")

        writer = csv.writer(archivo_salida)
        writer.writerow(["Apellido y Nombre", "Fecha de alta", "Domicilio"])

        while True:
            apellido_nombre_longitud = int(archivo_entrada.read(2))
            if not apellido_nombre_longitud:
                break
            apellido_nombre = archivo_entrada.read(apellido_nombre_longitud).strip()

            fecha_alta_longitud = int(archivo_entrada.read(2))
            fecha_alta = archivo_entrada.read(fecha_alta_longitud).strip()

            domicilio_longitud = int(archivo_entrada.read(2))
            domicilio = archivo_entrada.read(domicilio_longitud).strip()
            
            writer.writerow([apellido_nombre, fecha_alta, domicilio])

    except Exception as e:
        print(f"Error: {e}")
    finally:
        archivo_entrada.close()
        archivo_salida.close()



leer_formato_1("/mnt/data/empleados_formato_1.txt", "/mnt/data/empleados_formato_1.csv")
leer_formato_2("/mnt/data/empleados_formato_2.txt", "/mnt/data/empleados_formato_2.csv")





