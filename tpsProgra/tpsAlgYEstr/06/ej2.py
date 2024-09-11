'''Nombre: Rocco Moresi
Nombre problema: INSCRIBIR DEPORTISTAS
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:
Fecha: 22/06/2024

MODULOS:
'''
def grabarRangoAlturas(pathAlturas, d1,d2,d3):
    sumaDepo1 = 0
    sumaDepo2 = 0 
    sumaDepo3 = 0
    cantJugdep1 = int(input(f"Ingrese la cantidad de jugadores que van a ingresar en el deport {d1}: "))
    a = open(pathAlturas,"a",encoding="utf-8")
    a.write(d1)
    a.write("\n")
    for i in range(cantJugdep1):
        altura = int(input("Ingrese la altura de el jugador: "))  
        sumaDepo1+=altura 
        a.write(str(altura))
        a.write("\n")
    promDepo1 = sumaDepo1 // cantJugdep1
    a.write(d2)
    a.write("\n")
    cantJugDep2 = int(input(f"Ingrese la cantidad de jugadores que van a ingresar en el deport {d2}: "))
    for i in range(cantJugDep2):
        altura = int(input("Ingrese la altura de el jugador: "))
        sumaDepo2+=altura
        a.write(str(altura))
        a.write("\n")
    promDepo2 = sumaDepo2 // cantJugDep2
    a.write(d3)
    a.write("\n")
    cantJugDep3 = int(input(f"Ingrese la cantidad de jugadores que van a ingresar en el deport {d3}: "))
    for i in range(cantJugDep3):
        altura = int(input("Ingrese la altura de el jugador: "))
        sumaDepo3+=altura
        a.write(str(altura))
        a.write("\n")
    promDepo3 = sumaDepo3 // cantJugDep3
    a.close()
    
    return promDepo1,promDepo2,promDepo3

def grabarPromedio(pathAlturas, pathPromedios,d1,d2,d3,promDepo1,promDepo2,promDepo3):
    p = open(pathPromedios,"a",encoding="utf-8")
    p.write(d1)
    p.write("\n")
    p.write(str(promDepo1))
    p.write("\n")
    p.write(d2)
    p.write("\n")
    p.write(str(promDepo2))
    p.write("\n")
    p.write(d3)
    p.write("\n")
    p.write(str(promDepo3))
    p.close()    
    return

pathAlturas = "C:/m/ALTURAS.txt"
pathPromedios = "C:/m/PROMEDIOS.txt"
d1 = "Futbol"
d2 = "Hockey"
d3 = "Basquetball"

promDepo1,promDepo2,promDepo3= grabarRangoAlturas(pathAlturas, d1,d2,d3)
grabarPromedio(pathAlturas, pathPromedios,d1,d2,d3,promDepo1,promDepo2,promDepo3)