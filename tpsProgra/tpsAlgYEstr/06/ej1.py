'''
Nombre: Rocco Moresi
Nombre problema: APELLIDO POR PAIS
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:
Fecha: 21/06/2024

MODULOS:
'''


def terminadosEnIan(rutaG,rutaA,rutaE,rutaI):
    
    general = open(rutaG,"r",encoding="utf-8")
    
    for linea in general:
        x = linea.split(",")
        ian = x[0].endswith("ian")
        ini = x[0].endswith("ini")
        ez = x[0].endswith("ez")
        
        if ian == True:
            arm = open(rutaA,"a",encoding="utf-8")
            arm.write(linea)
            arm.close()
        elif ini == True:
            it = open(rutaI,"a",encoding="utf-8")
            it.write(linea)
            it.close()
        elif ez == True:
            esp = open(rutaE,"a",encoding="utf-8")
            esp.write(linea)
            esp.close()       
    
    general.close()
        
    
    return


rutaGeneral = "C:/m/GENERAL.txt"
rutaArmenia = "C:/m/ARMENIA.txt"
rutaEspaña = "C:/m/ESPAÑA.txt"
rutaItalia = "C:/m/ITALIA.txt"

terminadosEnIan(rutaGeneral,rutaArmenia,rutaEspaña,rutaItalia)


