import os, pymysql

import DAO.CRUDAsignacion_emp as CRUDAsignacion_emp
import DAO.CRUDDepartamento as CRUDDepartamento
import DAO.CRUDEmpleado as CRUDEmpleado
import DAO.CRUDProyecto as CRUDProyecto
import DAO.CRUDTiempo as CRUDTiempo
import DAO.CRUDValidaciones as CRUDValidaciones
from DTO.Empleado import Empleado





#Mostrar el menú principal
def mostrar_menu():
    print("========================================")
    print("          MENÚ PRINCIPAL          ")
    print("========================================")
    print("1. Gestión de Empleados")
    print("2. Gestión de Departamentos")
    print("3. Gestión de Proyectos")
    print("4. Registro de Tiempo")
    print("5. Asignación de Empleado a Proyectos")
    print("6. Generar Informe")
    print("7. Salir")
    print("========================================")


def menu_empleados():
    while True:
        print("\n--- GESTIÓN DE EMPLEADOS ---")
        print("1. Ingresar empleado")
        print("2. Mostrar empleados")
        print("3. Modificar empleado")
        print("4. Eliminar empleado")
        print("5. Volver al menú principal")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            ingresardatos()
        elif opcion == "2":
            mostrardatos()
        elif opcion == "3":
            modificardatos()
        elif opcion == "4":
            eliminardatos()
        elif opcion == "5":
            return
        else:
            print("Opción no válida.")

def menu_departamentos():
    print("\n--- GESTIÓN DE DEPARTAMENTOS ---")

def menu_proyectos():
    print("\n--- GESTIÓN DE PROYECTOS ---")

def menu_registro_tiempo():
    print("\n--- REGISTRO DE TIEMPO ---")

def menu_asignacion():
    print("\n--- ASIGNACIÓN DE EMPLEADO A PROYECTOS ---")

def menu_informe():
    print("\n--- GENERAR INFORME ---")

def main():
    while True:
        mostrar_menu()
        opcion = input("INGRESE OPCIÓN : ").strip()

        if opcion == "1":
            menu_empleados()
        elif opcion == "2":
            menu_departamentos()
        elif opcion == "3":
            menu_proyectos()
        elif opcion == "4":
            menu_registro_tiempo()
        elif opcion == "5":
            menu_asignacion()
        elif opcion == "6":
            menu_informe()
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\n[!] Opción no válida. Intente nuevamente.\n")

#--INGRESAR--
def ingresardatos():
    os.system('cls')

    print("======================")
    print("   INGRESAR EMPLEADO  ")
    print("======================")

    run = input("Ingrese RUN: ")
    nombre = input("Ingrese Nombre: ")
    direccion = input("Ingrese Dirección: ")
    telefono = input("Ingrese Teléfono: ")
    correo = input("Ingrese Correo: ")
    fecha_inicio = input("Ingrese Fecha de Inicio (YYYY-MM-DD): ")
    try:
        salario = float(input("Ingrese Salario: "))
        departamento_id = int(input("Ingrese ID del Departamento: "))
    except ValueError:
        print("El salario debe ser numérico y el ID del departamento debe ser un entero.")
        return

    empleado = Empleado(
        None,
        departamento_id,
        run,
        nombre,
        direccion,
        telefono,
        correo,
        fecha_inicio,
        salario,
    )

    if CRUDEmpleado.agregar(empleado):
        print("Empleado ingresado correctamente.")
    else:
        print("No se pudo ingresar el empleado.")


def mostrardatos():
    empleados = CRUDEmpleado.mostrartodos()
    if not empleados:
        print("No hay empleados para mostrar.")
        return

    print("\nID | RUN | Nombre | Dirección | Teléfono | Correo | Fecha inicio | Salario | Departamento")
    print("-" * 110)
    for empleado in empleados:
        print(
            f"{empleado[0]} | {empleado[1]} | {empleado[2]} | {empleado[3]} | "
            f"{empleado[4]} | {empleado[5]} | {empleado[6]} | {empleado[7]} | {empleado[8]}"
        )


def modificardatos():
    try:
        empleado_id = int(input("ID del empleado a modificar: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    actual = CRUDEmpleado.consultarparticular(empleado_id)
    if actual is None:
        print("No se encontró un empleado con ese ID.")
        return

    print("Deje un campo vacío para conservar su valor actual.")
    run = input(f"RUN [{actual[1]}]: ").strip() or actual[1]
    nombre = input(f"Nombre [{actual[2]}]: ").strip() or actual[2]
    direccion = input(f"Dirección [{actual[3]}]: ").strip() or actual[3]
    telefono = input(f"Teléfono [{actual[4]}]: ").strip() or actual[4]
    correo = input(f"Correo [{actual[5]}]: ").strip() or actual[5]
    fecha_inicio = input(f"Fecha de inicio [{actual[6]}]: ").strip() or actual[6]

    try:
        salario_texto = input(f"Salario [{actual[7]}]: ").strip()
        salario = float(salario_texto) if salario_texto else float(actual[7])
        departamento_texto = input(f"ID del departamento [{actual[8]}]: ").strip()
        departamento_id = int(departamento_texto) if departamento_texto else int(actual[8])
    except (TypeError, ValueError):
        print("El salario debe ser numérico y el ID del departamento debe ser un entero.")
        return

    empleado = Empleado(
        actual[0],
        departamento_id,
        run,
        nombre,
        direccion,
        telefono,
        correo,
        fecha_inicio,
        salario,
    )

    if CRUDEmpleado.editar(empleado):
        print("Empleado modificado correctamente.")
    else:
        print("No se pudo modificar el empleado.")


def eliminardatos():
    try:
        empleado_id = int(input("ID del empleado a eliminar: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    empleado = CRUDEmpleado.consultarparticular(empleado_id)
    if empleado is None:
        print("No se encontró un empleado con ese ID.")
        return

    confirmacion = input(f"¿Eliminar a {empleado[2]}? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Eliminación cancelada.")
        return

    if CRUDEmpleado.eliminar(empleado_id):
        print("Empleado eliminado correctamente.")
    else:
        print("No se pudo eliminar el empleado.")


if __name__ == "__main__":
    main()
    