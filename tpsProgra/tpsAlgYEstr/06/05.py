'''
Nombre: Rocco Moresi
Nombre problema: HOTEL Y RESERVAS
Materia: algoritmos y estructuras de datos 1
LU: 1185425
Descripcion:
Fecha: 27/06/2024

MODULOS:
'''

import csv
import datetime

def es_fecha_valida(fecha):
    try:
        datetime.datetime.strptime(fecha, "%d%m%Y")
        return True
    except ValueError:
        return False

def dias_entre_fechas(fecha1, fecha2):
    fecha1 = datetime.datetime.strptime(fecha1, "%d%m%Y")
    fecha2 = datetime.datetime.strptime(fecha2, "%d%m%Y")
    return (fecha2 - fecha1).days

def registrar_huespedes():
    archivo = open("huespedes.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(archivo)
    writer.writerow(["DNI", "Apellido y Nombre", "Fecha de Ingreso", "Fecha de Egreso", "Cantidad de Ocupantes"])

    dnis = set()

    while True:
        dni = int(input("Ingrese DNI del huésped (o -1 para finalizar): "))
        if dni == -1:
            break
        if dni in dnis:
            print("El DNI ya está registrado.")
            continue
        
        apellido_nombre = input("Ingrese Apellido y Nombre: ")
        fecha_ingreso = input("Ingrese Fecha de Ingreso (DDMMAAAA): ")
        fecha_egreso = input("Ingrese Fecha de Egreso (DDMMAAAA): ")
        if not es_fecha_valida(fecha_ingreso) or not es_fecha_valida(fecha_egreso):
            print("Fecha no válida.")
            continue
        if dias_entre_fechas(fecha_ingreso, fecha_egreso) <= 0:
            print("La fecha de egreso debe ser mayor a la de ingreso.")
            continue
        
        cantidad_ocupantes = int(input("Ingrese la cantidad de ocupantes: "))
        
        writer.writerow([dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes])
        dnis.add(dni)

    archivo.close()

def asignar_habitaciones():
    with open("huespedes.csv", "r", encoding="utf-8") as archivo:
        reader = csv.reader(archivo)
        next(reader)  

        habitaciones = [[None for _ in range(6)] for _ in range(10)]
        huespedes = []

        for fila in reader:
            dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes = fila
            asignado = False
            for piso in range(10):
                for hab in range(6):
                    if habitaciones[piso][hab] is None:
                        habitaciones[piso][hab] = fila
                        huespedes.append((fila, piso, hab))
                        asignado = True
                        break
                if asignado:
                    break

    return habitaciones, huespedes

def mostrar_piso_con_mayor_ocupacion(habitaciones):
    max_ocupadas = 0
    piso_mayor_ocupacion = None
    for piso in range(10):
        ocupadas = sum(1 for hab in habitaciones[piso] if hab is not None)
        if ocupadas > max_ocupadas:
            max_ocupadas = ocupadas
            piso_mayor_ocupacion = piso + 1
    print(f"El piso con mayor cantidad de habitaciones ocupadas es el piso {piso_mayor_ocupacion}")

def mostrar_habitaciones_vacias(habitaciones):
    vacias = sum(1 for piso in habitaciones for hab in piso if hab is None)
    print(f"Hay {vacias} habitaciones vacías en todo el hotel.")

def mostrar_piso_con_mas_personas(habitaciones):
    max_personas = 0
    piso_mas_personas = None
    for piso in range(10):
        personas = sum(int(hab[4]) for hab in habitaciones[piso] if hab is not None)
        if personas > max_personas:
            max_personas = personas
            piso_mas_personas = piso + 1
    print(f"El piso con mayor cantidad de personas es el piso {piso_mas_personas}")

def mostrar_proxima_habitacion_en_desocuparse(habitaciones):
    fecha_actual = input("Ingrese la fecha actual (DDMMAAAA): ")
    if not es_fecha_valida(fecha_actual):
        print("Fecha no válida.")
        return

    proxima_fecha = None
    proximas_habitaciones = []

    for piso in range(10):
        for hab in range(6):
            if habitaciones[piso][hab] is not None:
                fecha_egreso = habitaciones[piso][hab][3]
                if proxima_fecha is None or fecha_egreso < proxima_fecha:
                    proxima_fecha = fecha_egreso
                    proximas_habitaciones = [(piso + 1, hab + 1)]
                elif fecha_egreso == proxima_fecha:
                    proximas_habitaciones.append((piso + 1, hab + 1))

    if proximas_habitaciones:
        print(f"La(s) próxima(s) habitación(es) en desocuparse será(n) el {proxima_fecha}:")
        for piso, hab in proximas_habitaciones:
            print(f"Piso {piso}, Habitación {hab}")

def mostrar_huespedes_ordenados_por_estadia(huespedes):
    huespedes_ordenados = sorted(huespedes, key=lambda x: dias_entre_fechas(x[0][2], x[0][3]), reverse=True)
    print("Huéspedes ordenados por cantidad de días de alojamiento:")
    for huesped, piso, hab in huespedes_ordenados:
        dni, apellido_nombre, fecha_ingreso, fecha_egreso, cantidad_ocupantes = huesped
        dias = dias_entre_fechas(fecha_ingreso, fecha_egreso)
        print(f"DNI: {dni}, Nombre: {apellido_nombre}, Días: {dias}, Habitación: Piso {piso + 1}, Habitación {hab + 1}")


registrar_huespedes()
habitaciones, huespedes = asignar_habitaciones()
mostrar_piso_con_mayor_ocupacion(habitaciones)
mostrar_habitaciones_vacias(habitaciones)
mostrar_piso_con_mas_personas(habitaciones)
mostrar_proxima_habitacion_en_desocuparse(habitaciones)
mostrar_huespedes_ordenados_por_estadia(huespedes)

