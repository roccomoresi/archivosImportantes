'''
Nombre: Rocco Moresi
Nombre problema:  ELIMINAR COMENTARIOS
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python. Tener en cuenta
que los comentarios comienzan con el signo # (siempre que éste no se encuentre encerrado entre comillas simples o
dobles) y que también se considera comentario a las cadenas de documentación (docstrings).
Fecha: 27/06/2024

MODULOS:
'''



def borrarDocsSYComents(ruta_lectura, ruta_escritura):
    with open(ruta_lectura, "r", encoding="utf-8") as archivo_lectura:
        lineas = archivo_lectura.readlines()

    lineas_filtradas = []
    en_comentario_bloque = False

    for linea in lineas:
       
        if "'''" in linea or '"""' in linea:
            en_comentario_bloque = not en_comentario_bloque
            continue
        
       
        if en_comentario_bloque:
            continue

        
        if "#" in linea:
            indice = linea.index("#")
            linea = linea[:indice].strip()
        
   
        if linea.strip():
            lineas_filtradas.append(linea + '\n')

    with open(ruta_escritura, "w", encoding="utf-8") as archivo_escritura:
        archivo_escritura.writelines(lineas_filtradas)


ruta_lectura = "C:/m/xd.py"
ruta_escritura = "C:/m/xd.py"

borrarDocsSYComents(ruta_lectura, ruta_escritura)

