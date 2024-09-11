'''
Nombre: Rocco Moresi
Nombre problema:    REMOVE SOBRE CONJUNTOS
Materia: algoritmos y estructuras de datos 1
LU: 1185425

Descripcion: Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al usuario y eliminarlos del conjunto mediante
el método remove, mostrando el contenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.



Fecha: 27/06/2024

MODULOS:
'''
try:
    conj = set([0,1])
    num = int(input("Ingrese numero que quiere eliminar de la lista: "))
    conj.remove(num)
    print(conj)


    while num != -1:
        if len(conj) == 0:
            print("CONJUTO VACIO")
        num = int(input("Ingrese numero que quiere eliminar de la lista: "))
        conj.remove(num)
        print(conj)
except KeyError:
    print("Valor fuera de rango o inexistente en el conjunto.")




