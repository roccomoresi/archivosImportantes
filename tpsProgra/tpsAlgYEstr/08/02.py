'''
Nombre: Rocco Moresi
Nombre problema:  DESCOMPOSICIÓN DE EMAIL
Materia: algoritmos y estructuras de datos 1
LU: 1185425

Descripcion:Desarrollar un programa que utilice una función que reciba como parámetro una cadena de caracteres conteniendo una
dirección de correo electrónico y devuelva una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar)


Fecha: 21/06/2024

MODULOS:
'''

def email(cadena):
    c = cadena.split("@")
    g = c[1].split(".")
    c.pop()
    c.append(g[0])
    c.append(g[1])
    tu = tuple(c)
    
    return tu

mail = "roccomoresi@uade.ar"
if "@" not in mail or "." not in mail:
    print("Mail incorrecto")
else:
    c = email(mail)
    print(c)

