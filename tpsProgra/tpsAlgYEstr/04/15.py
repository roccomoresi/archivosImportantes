'''
Nombre: Rocco Moresi
Nombre problema:  NUMERO A LETRAS



Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:Muchas aplicaciones financieras requieren que los números sean expresados también en letras. Por ejemplo, el número
2153 puede escribirse como "dos mil ciento cincuenta y tres". Nos piden un programa con una función para convertir a
texto un número entero entre 0 y casi mil millones (es decir, cifras hasta 999.999.999).
Revisando módulos desarrollados en el pasado por nuestro equipo de programadores encontramos una función para
convertir números a texto, pero preparada para valores entre 0 y 999.999 (el profesor entregará esta función). Analizar
la función recuperada y realizarle los cambios necesarios para que funcione hasta 999.999.999







Fecha: 09/07/2024

MODULOS:
'''

def numero_a_letras(numero):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    miles = ["mil", "millón", "millones"]


    def convertir_menos_mil(num):
        if num < 10:
            return unidades[num]
        elif num < 20:
            return especiales[num - 10]
        else:
            u = num % 10
            d = num // 10
            if u == 0:
                return decenas[d]
            else:
                return decenas[d] + " y " + unidades[u]

    if numero == 0:
        return "cero"

    resultado = ""
    millones = numero // 1000000
    numero = numero % 1000000
    miles_millones = ""
    
    if millones == 1:
        miles_millones = "millón"
    elif millones > 1:
        miles_millones = "millones"

    if millones > 0:
        resultado += convertir_menos_mil(millones) + " " + miles_millones + " "

    miles = numero // 1000
    numero = numero % 1000

    if miles > 0:
        if miles == 1:
            resultado += "mil "
        else:
            resultado += convertir_menos_mil(miles) + " mil "

    if numero > 0:
        resultado += convertir_menos_mil(numero)

    return resultado.strip()


numeros = [0, 1, 10, 15, 100, 101, 999, 1000, 2153, 999999, 1234567, 999999999]

for numero in numeros:
    print(f"{numero}: {numero_a_letras(numero)}")
