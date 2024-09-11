'''
Nombre: Rocco Moresi
Nombre problema:   BARAJA ESPAÑOLA



Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Escribir un programa para crear mediante listas por comprensión los naipes de la baraja española de 48 cartas. La lista
debe contener cadenas de caracteres. Ejemplo: ["1 de Oros", "2 de Oros"... ]. Imprimir la lista por pantalla. (investigar en
internet el tema “python listas por comprensión producto cartesiano de dos listas”)





Fecha: 09/07/2024

MODULOS:
'''


baraja_española = [
    f"{numero} de {palo}"
    for palo in ["Oros", "Copas", "Espadas", "Bastos"]
    for numero in ["1", "2", "3", "4", "5", "6", "7", "Sota", "Caballo", "Rey"]
]


for carta in baraja_española:
    print(carta)
