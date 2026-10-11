import os, pymysql

import DAO.CRUDAsignacion_emp as CRUDAsignacion_emp
import DAO.CRUDDepartamento as CRUDDepartamento
import DAO.CRUDEmpleado as CRUDEmpleado
import DAO.CRUDProyecto as CRUDProyecto
import DAO.CRUDTiempo as CRUDTiempo
import DAO.CRUDValidaciones as CRUDValidaciones
from DTO.Empleado import Empleado
from DTO.Departamento import Departamento
from DTO.Proyecto import Proyecto
from DTO.RegistroTiempo import RegistroTiempo
from DTO.Asignacion import Asignacion


#Mostrar el menú principal
def mostrar_menu():
    os.system('cls')
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
    while True:
        print("\n--- GESTIÓN DE DEPARTAMENTOS ---")
        print("1. Ingresar departamento")
        print("2. Mostrar departamentos")
        print("3. Modificar departamento")
        print("4. Eliminar departamento")
        print("5. Volver al menú principal")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1": ingresar_depto()
        elif opcion == "2": mostrar_deptos()
        elif opcion == "3": modificar_depto()
        elif opcion == "4": eliminar_depto()
        elif opcion == "5": return
        else: print("Opción no válida.")

def menu_proyectos():
    while True:
        print("\n--- GESTIÓN DE PROYECTOS ---")
        print("1. Ingresar proyecto")
        print("2. Mostrar proyectos")
        print("3. Modificar proyecto")
        print("4. Eliminar proyecto")
        print("5. Volver al menú principal")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1": ingresar_proyecto()
        elif opcion == "2": mostrar_proyectos()
        elif opcion == "3": modificar_proyecto()
        elif opcion == "4": eliminar_proyecto()
        elif opcion == "5": return
        else: print("Opción no válida.")

def menu_registro_tiempo():
    while True:
        print("\n--- REGISTRO DE TIEMPO ---")
        print("1. Registrar horas")
        print("2. Mostrar registros de tiempo")
        print("3. Modificar registro")
        print("4. Eliminar registro")
        print("5. Volver al menú principal")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1": ingresar_tiempo()
        elif opcion == "2": mostrar_tiempos()
        elif opcion == "3": modificar_tiempo()
        elif opcion == "4": eliminar_tiempo()
        elif opcion == "5": return
        else: print("Opción no válida.")

def menu_asignacion():
    while True:
        print("\n--- ASIGNACIÓN DE EMPLEADO A PROYECTOS ---")
        print("1. Asignar empleado a proyecto")
        print("2. Mostrar asignaciones")
        print("3. Modificar asignación")
        print("4. Eliminar asignación")
        print("5. Volver al menú principal")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1": ingresar_asignacion()
        elif opcion == "2": mostrar_asignaciones()
        elif opcion == "3": modificar_asignacion()
        elif opcion == "4": eliminar_asignacion()
        elif opcion == "5": return
        else: print("Opción no válida.")

def menu_informe():
    print("\n--- GENERAR INFORME ---")
    print("Módulo de informes en construcción...")
    input("Presione Enter para continuar...")

def main():
    while True:
        mostrar_menu()
        opcion = input("INGRESE OPCIÓN : ").strip()

        if opcion == "1": menu_empleados()
        elif opcion == "2": menu_departamentos()
        elif opcion == "3": menu_proyectos()
        elif opcion == "4": menu_registro_tiempo()
        elif opcion == "5": menu_asignacion()
        elif opcion == "6": menu_informe()
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\n[!] Opción no válida. Intente nuevamente.\n")


# ==========================================
# CRUD EMPLEADOS 
# ==========================================

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
        None, departamento_id, run, nombre, direccion, telefono, correo, fecha_inicio, salario
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
    for emp in empleados:
        print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4]} | {emp[5]} | {emp[6]} | {emp[7]} | {emp[8]}")

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
        sal_txt = input(f"Salario [{actual[7]}]: ").strip()
        salario = float(sal_txt) if sal_txt else float(actual[7])
        dep_txt = input(f"ID del departamento [{actual[8]}]: ").strip()
        departamento_id = int(dep_txt) if dep_txt else int(actual[8])
    except ValueError:
        print("El salario debe ser numérico y el ID del departamento debe ser un entero.")
        return

    empleado = Empleado(
        actual[0], departamento_id, run, nombre, direccion, telefono, correo, fecha_inicio, salario
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
    if confirmacion == "s":
        if CRUDEmpleado.eliminar(empleado_id):
            print("Empleado eliminado correctamente.")
        else:
            print("No se pudo eliminar el empleado.")


# ==========================================
# CRUD DEPARTAMENTOS
# ==========================================

def ingresar_depto():
    os.system('cls')
    print("\n--- INGRESAR DEPARTAMENTO ---")
    nombre = input("Ingrese Nombre del Departamento: ")
    descripcion = input("Ingrese Descripción: ")
    try:
        gerente_id = input("Ingrese ID del Empleado Gerente (o deje en blanco): ").strip()
        gerente_emp_id = int(gerente_id) if gerente_id else None
    except ValueError:
        print("El ID del gerente debe ser un número entero.")
        return

    # Se pasa None como ID inicial ya que es autoincremental
    d = Departamento(None, nombre, descripcion, gerente_emp_id)
    
    if CRUDDepartamento.agregar(d):
        print("Departamento ingresado correctamente.")
    else:
        print("Error al ingresar departamento.")

def mostrar_deptos():
    deptos = CRUDDepartamento.mostrartodos()
    if not deptos:
        print("No hay departamentos para mostrar.")
        return
    print("\nID | Nombre | Descripción | ID Gerente | Nombre Gerente")
    print("-" * 60)
    for d in deptos:
        print(f"{d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]}")

def modificar_depto():
    try:
        depto_id = int(input("ID del departamento a modificar: "))
    except ValueError:
        print("El ID debe ser entero.")
        return
    
    actual = CRUDDepartamento.consultarparticular(depto_id) 
    if not actual:
        print("No se encontró el departamento.")
        return

    print("Deje un campo vacío para conservar su valor actual.")
    nombre = input(f"Nombre [{actual[1]}]: ").strip() or actual[1]
    descripcion = input(f"Descripción [{actual[2]}]: ").strip() or actual[2]
    try:
        ger_txt = input(f"ID Gerente [{actual[3]}]: ").strip()
        gerente_emp_id = int(ger_txt) if ger_txt else actual[3]
    except ValueError:
        print("Error de formato numérico.")
        return

    d = Departamento(depto_id, nombre, descripcion, gerente_emp_id)
    
    if CRUDDepartamento.editar(d):
        print("Departamento modificado.")
    else:
        print("Error al modificar.")

def eliminar_depto():
    try:
        depto_id = int(input("ID del departamento a eliminar: "))
    except ValueError:
        print("El ID debe ser entero.")
        return
    if CRUDDepartamento.eliminar(depto_id):
        print("Departamento eliminado.")
    else:
        print("No se pudo eliminar.")


# ==========================================
# CRUD PROYECTOS
# ==========================================

def ingresar_proyecto():
    os.system('cls')
    print("\n--- INGRESAR PROYECTO ---")
    nombre = input("Nombre del Proyecto: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")

    p = Proyecto(None, nombre, descripcion, fecha_inicio)
    
    if CRUDProyecto.agregar(p):
        print("Proyecto registrado.")
    else:
        print("Error al registrar proyecto.")

def mostrar_proyectos():
    proys = CRUDProyecto.mostrartodos()
    if not proys:
        print("No hay proyectos.")
        return
    print("\nID | Nombre | Descripción | Fecha de inicio")
    print("-" * 60)
    for p in proys:
        print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]}")

def modificar_proyecto():
    try:
        proy_id = int(input("ID del proyecto a modificar: "))
    except ValueError:
        print("ID debe ser numérico.")
        return
    
    actual = CRUDProyecto.consultarparticular(proy_id)
    if not actual:
        print("Proyecto no encontrado.")
        return
    
    print("Deje un campo vacío para conservar su valor actual.")
    nombre = input(f"Nombre [{actual[1]}]: ").strip() or actual[1]
    descripcion = input(f"Descripción [{actual[2]}]: ").strip() or actual[2]
    fecha = input(f"Fecha [{actual[3]}]: ").strip() or actual[3]

    p = Proyecto(proy_id, nombre, descripcion, fecha)
    
    if CRUDProyecto.editar(p):
        print("Proyecto modificado.")
    else:
        print("Error al modificar.")

def eliminar_proyecto():
    try:
        proy_id = int(input("ID del proyecto a eliminar: "))
    except ValueError:
        print("El ID debe ser entero.")
        return
    if CRUDProyecto.eliminar(proy_id):
        print("Proyecto eliminado.")
    else:
        print("No se pudo eliminar.")


# ==========================================
# CRUD TIEMPO (Horas Trabajadas)
# ==========================================

def ingresar_tiempo():
    os.system('cls')
    print("\n--- REGISTRAR TIEMPO ---")
    try:
        emp_id = int(input("ID del Empleado: "))
        proy_id = int(input("ID del Proyecto: "))
        fecha = input("Fecha (YYYY-MM-DD): ")
        horas = float(input("Horas Trabajadas: "))
    except ValueError:
        print("ID numérico y horas en formato decimal.")
        return
    descripcion = input("Descripción de tarea: ")

    t = Tiempo(None, emp_id, proy_id, fecha, horas, descripcion)
    
    if CRUDTiempo.agregar(t):
        print("Tiempo registrado correctamente.")
    else:
        print("Error al registrar.")

def mostrar_tiempos():
    tiempos = CRUDTiempo.mostrartodos()
    if not tiempos:
        print("No hay registros de tiempo.")
        return
    print("\nID Reg. | Empleado | Proyecto | Fecha | Horas | Descripción")
    print("-" * 80)
    for t in tiempos:
        print(f"{t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]} | {t[5]}")

def modificar_tiempo():
    try:
        t_id = int(input("ID del Registro de Tiempo a modificar: "))
    except ValueError:
        print("El ID debe ser entero.")
        return
    
    actual = CRUDTiempo.consultarparticular(t_id)
    if not actual:
        print("Registro no encontrado.")
        return
    
    try:
        emp_txt = input(f"ID Empleado [{actual[1]}]: ").strip()
        emp_id = int(emp_txt) if emp_txt else actual[1]
        proy_txt = input(f"ID Proyecto [{actual[2]}]: ").strip()
        proy_id = int(proy_txt) if proy_txt else actual[2]
        fecha = input(f"Fecha [{actual[3]}]: ").strip() or actual[3]
        hrs_txt = input(f"Horas [{actual[4]}]: ").strip()
        horas = float(hrs_txt) if hrs_txt else actual[4]
    except ValueError:
        print("Error de formato numérico.")
        return
    descripcion = input(f"Descripción [{actual[5]}]: ").strip() or actual[5]

    t = Tiempo(t_id, emp_id, proy_id, fecha, horas, descripcion)
    
    if CRUDTiempo.editar(t):
        print("Registro de tiempo modificado.")
    else:
        print("Error al modificar.")

def eliminar_tiempo():
    try:
        t_id = int(input("ID del registro a eliminar: "))
    except ValueError:
        print("El ID debe ser entero.")
        return
    if CRUDTiempo.eliminar(t_id):
        print("Registro eliminado.")
    else:
        print("No se pudo eliminar.")


# ==========================================
# CRUD ASIGNACIÓN (Empleado - Proyecto)
# ==========================================

def ingresar_asignacion():
    os.system('cls')
    print("\n--- ASIGNAR EMPLEADO A PROYECTO ---")
    try:
        emp_id = int(input("ID del Empleado: "))
        proy_id = int(input("ID del Proyecto: "))
    except ValueError:
        print("Los IDs deben ser números enteros.")
        return
    rol = input("Rol a desempeñar: ")
    fecha = input("Fecha de inicio (YYYY-MM-DD): ")

    a = Asignacion(emp_id, proy_id, rol, fecha)
    
    if CRUDAsignacion_emp.agregar(a):
        print("Asignación completada.")
    else:
        print("Error al asignar.")

def mostrar_asignaciones():
    asig = CRUDAsignacion_emp.mostrartodos()
    if not asig:
        print("No hay asignaciones registradas.")
        return
    print("\nID Emp. | Empleado | ID Proy. | Proyecto | Rol | Fecha Inicio")
    print("-" * 80)
    for a in asig:
        print(f"{a[0]} | {a[1]} | {a[2]} | {a[3]} | {a[4]} | {a[5]}")

def modificar_asignacion():
    print("\n--- MODIFICAR ROL DE ASIGNACIÓN ---")
    try:
        emp_id = int(input("ID del Empleado: "))
        proy_id = int(input("ID del Proyecto: "))
    except ValueError:
        print("Los IDs deben ser números enteros.")
        return

    actual = CRUDAsignacion_emp.consultarparticular(emp_id, proy_id)
    if not actual:
        print("No se encontró esa combinación Empleado-Proyecto.")
        return

    rol = input(f"Nuevo Rol [{actual[2]}]: ").strip() or actual[2]
    fecha = input(f"Nueva Fecha de Inicio [{actual[3]}]: ").strip() or actual[3]

    a = Asignacion(emp_id, proy_id, rol, fecha)
    
    if CRUDAsignacion_emp.editar(a):
        print("Asignación modificada.")
    else:
        print("Error al modificar.")

def eliminar_asignacion():
    print("\n--- ELIMINAR ASIGNACIÓN ---")
    try:
        emp_id = int(input("ID del Empleado a desvincular: "))
        proy_id = int(input("ID del Proyecto: "))
    except ValueError:
        print("Los IDs deben ser números enteros.")
        return
    
    if CRUDAsignacion_emp.eliminar(emp_id, proy_id):
        print("Asignación eliminada correctamente.")
    else:
        print("No se pudo eliminar.")


if __name__ == "__main__":
    main()