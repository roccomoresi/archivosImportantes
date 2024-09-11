'''
Nombre: Rocco Moresi
Nombre problema: VERIFICACIÓN DE DIRECCIÓN DE EMAIL



Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Se solicita crear un programa para leer direcciones de correo electrónico y verificar si representan una dirección válida.
Por ejemplo usuario@dominio.com.ar. Para que una dirección sea considerada válida el nombre de usuario debe poseer solamente caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe tener al menos un carácter
y tiene que finalizar con “.com.ar”
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mostrar un listado de todos los dominios, sin
repetirlos y ordenados alfabéticamente, recordando que las direcciones de mail no son case sensitive.






Fecha: 09/07/2024

MODULOS:
'''

def es_direccion_valida(email):
    partes = email.split('@')
    if len(partes) != 2:
        return False
    username, dominio = partes
    if not username.isalnum():
        return False
    if dominio.lower().endswith('.com.ar'):
        return True
    return False

def main():
    dominios = set()
    
    while True:
        email = input("Ingrese una dirección de correo electrónico (o vacío para terminar): ").strip()
        if email == "":
            break
        
        if es_direccion_valida(email):
            _, dominio = email.split('@')
            dominios.add(dominio.lower())
        else:
            print(f"Dirección de correo electrónico '{email}' no válida.")

    print("\nListado de dominios válidos:")
    for dominio in sorted(dominios):
        print(dominio)

if __name__ == "__main__":
    main()
