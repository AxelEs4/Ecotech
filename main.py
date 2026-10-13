import os

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
from DTO.Asignacion import AsignacionEmp


# ==========================================
# MENÚS PRINCIPALES Y SUBMENÚS
# ==========================================

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

        if opcion == "1": ingresardatos()
        elif opcion == "2": mostrardatos()
        elif opcion == "3": modificardatos()
        elif opcion == "4": eliminardatos()
        elif opcion == "5": return
        else: print("Opción no válida.")

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
    os.system('cls')
    print("==================================================")
    print("             INFORME GENERAL ECOTECH              ")
    print("==================================================")

    # Recopilamos los datos usando los DAOs existentes para mostrar totales
    empleados = CRUDEmpleado.mostrartodos()
    deptos = CRUDDepartamento.mostrartodos()
    proyectos = CRUDProyecto.mostrartodos()
    asignaciones = CRUDAsignacion_emp.mostrartodos()

    print(f"Total de Empleados Registrados  : {len(empleados)}")
    print(f"Total de Departamentos Activos  : {len(deptos)}")
    print(f"Total de Proyectos en Curso     : {len(proyectos)}")
    print(f"Total de Asignaciones Activas   : {len(asignaciones)}")
    print("==================================================")
    
    input("\nPresione Enter para volver al menú principal...")

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
# CRUD EMPLEADOS (PK: run)
# ==========================================

def ingresardatos():
    os.system('cls')
    print("======================")
    print("   INGRESAR EMPLEADO  ")
    print("======================")

    run = input("Ingrese RUN: ")
    if CRUDValidaciones.existe_empleado(run):
        print("Error: Ya existe un empleado registrado con este RUN.")
        input("Presione Enter para continuar...")
        return

    nombre = input("Ingrese Nombre: ")
    direccion = input("Ingrese Dirección: ")
    telefono = input("Ingrese Teléfono: ")
    correo = input("Ingrese Correo: ")
    fecha_inicio = input("Ingrese Fecha de Inicio (YYYY-MM-DD): ")
    
    if not CRUDValidaciones.validar_fecha(fecha_inicio):
        print("Error: El formato de fecha no es válido.")
        input("Presione Enter para continuar...")
        return

    try:
        salario = float(input("Ingrese Salario: "))
        departamento_id = int(input("Ingrese ID del Departamento (numérico): "))
    except ValueError:
        print("Error: El salario debe ser numérico y el ID del departamento debe ser un entero.")
        input("Presione Enter para continuar...")
        return

    # Constructor INACAP: (run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id)
    empleado = Empleado(run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id)

    if CRUDEmpleado.agregar(empleado):
        print("Empleado ingresado correctamente.")
    else:
        print("No se pudo ingresar el empleado.")
    input("Presione Enter para continuar...")

def mostrardatos():
    empleados = CRUDEmpleado.mostrartodos()
    if not empleados:
        print("No hay empleados para mostrar.")
        input("Presione Enter para continuar...")
        return

    print("\nRUN | Nombre | Dirección | Teléfono | Correo | Fecha inicio | Salario | Depto ID")
    print("-" * 100)
    for emp in empleados:
        print(f"{emp[0]} | {emp[1]} | {emp[2]} | {emp[3]} | {emp[4]} | {emp[5]} | {emp[6]} | {emp[7]}")
    input("Presione Enter para continuar...")

def modificardatos():
    run_actual = input("Ingrese el RUN del empleado a modificar: ").strip()
    
    actual = CRUDEmpleado.consultarparticular(run_actual)
    if actual is None:
        print("No se encontró un empleado con ese RUN.")
        input("Presione Enter para continuar...")
        return

    print("Deje un campo vacío y presione Enter para conservar su valor actual.")
    nombre = input(f"Nombre [{actual[1]}]: ").strip() or actual[1]
    direccion = input(f"Dirección [{actual[2]}]: ").strip() or actual[2]
    telefono = input(f"Teléfono [{actual[3]}]: ").strip() or actual[3]
    correo = input(f"Correo [{actual[4]}]: ").strip() or actual[4]
    fecha_inicio = input(f"Fecha de inicio [{actual[5]}]: ").strip() or actual[5]

    try:
        sal_txt = input(f"Salario [{actual[6]}]: ").strip()
        salario = float(sal_txt) if sal_txt else float(actual[6])
        dep_txt = input(f"ID del departamento [{actual[7]}]: ").strip()
        departamento_id = int(dep_txt) if dep_txt else int(actual[7])
    except ValueError:
        print("Error: El salario debe ser numérico y el ID del departamento debe ser un entero.")
        input("Presione Enter para continuar...")
        return

    # Constructor INACAP
    empleado = Empleado(run_actual, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id)

    if CRUDEmpleado.editar(empleado):
        print("Empleado modificado correctamente.")
    else:
        print("No se pudo modificar el empleado.")
    input("Presione Enter para continuar...")

def eliminardatos():
    run = input("Ingrese el RUN del empleado a eliminar: ").strip()

    empleado = CRUDEmpleado.consultarparticular(run)
    if empleado is None:
        print("No se encontró un empleado con ese RUN.")
        input("Presione Enter para continuar...")
        return

    confirmacion = input(f"¿Eliminar a {empleado[1]}? (s/n): ").strip().lower()
    if confirmacion == "s":
        if CRUDEmpleado.eliminar(run):
            print("Empleado eliminado correctamente.")
        else:
            print("No se pudo eliminar el empleado.")
    input("Presione Enter para continuar...")


# ==========================================
# CRUD DEPARTAMENTOS (PK: nombre)
# ==========================================

def ingresar_depto():
    os.system('cls')
    print("\n--- INGRESAR DEPARTAMENTO ---")
    nombre = input("Ingrese Nombre del Departamento: ")
    if CRUDValidaciones.existe_departamento(nombre):
        print("Error: Ya existe un departamento con ese nombre.")
        input("Presione Enter para continuar...")
        return

    descripcion = input("Ingrese Descripción: ")
    try:
        gerente_id = input("Ingrese ID del Empleado Gerente (o deje en blanco): ").strip()
        gerente_emp_id = int(gerente_id) if gerente_id else 0
    except ValueError:
        print("El ID del gerente debe ser un número entero.")
        input("Presione Enter para continuar...")
        return

    # Constructor INACAP: (nombre, gerente_empleado_id, descripcion)
    d = Departamento(nombre, gerente_emp_id, descripcion)
    
    if CRUDDepartamento.agregar(d):
        print("Departamento ingresado correctamente.")
    else:
        print("Error al ingresar departamento.")
    input("Presione Enter para continuar...")

def mostrar_deptos():
    deptos = CRUDDepartamento.mostrartodos()
    if not deptos:
        print("No hay departamentos para mostrar.")
        input("Presione Enter para continuar...")
        return
    print("\nNombre | Descripción | ID Gerente | User ID Interno")
    print("-" * 60)
    for d in deptos:
        print(f"{d[0]} | {d[1]} | {d[2]} | {d[3]}")
    input("Presione Enter para continuar...")

def modificar_depto():
    nombre_actual = input("Nombre exacto del departamento a modificar: ").strip()
    actual = CRUDDepartamento.consultarparticular(nombre_actual) 
    if not actual:
        print("No se encontró el departamento.")
        input("Presione Enter para continuar...")
        return

    print("Deje un campo vacío para conservar su valor actual.")
    descripcion = input(f"Descripción [{actual[1]}]: ").strip() or actual[1]
    try:
        ger_txt = input(f"ID Gerente [{actual[2]}]: ").strip()
        gerente_emp_id = int(ger_txt) if ger_txt else actual[2]
    except ValueError:
        print("Error de formato numérico.")
        input("Presione Enter para continuar...")
        return

    # Se mantiene el user_id interno de la BD
    user_id_bd = actual[3]
    d = Departamento(nombre_actual, gerente_emp_id, descripcion, user_id_bd)
    
    if CRUDDepartamento.editar(d):
        print("Departamento modificado.")
    else:
        print("Error al modificar.")
    input("Presione Enter para continuar...")

def eliminar_depto():
    nombre = input("Nombre exacto del departamento a eliminar: ").strip()
    if CRUDDepartamento.eliminar(nombre):
        print("Departamento eliminado.")
    else:
        print("No se pudo eliminar.")
    input("Presione Enter para continuar...")


# ==========================================
# CRUD PROYECTOS (PK: user_id)
# ==========================================

def ingresar_proyecto():
    os.system('cls')
    print("\n--- INGRESAR PROYECTO ---")
    nombre = input("Nombre del Proyecto: ")
    descripcion = input("Descripción: ")
    fecha_inicio = input("Fecha de Inicio (YYYY-MM-DD): ")

    if not CRUDValidaciones.validar_fecha(fecha_inicio):
        print("Error: El formato de fecha no es válido.")
        input("Presione Enter para continuar...")
        return

    p = Proyecto(nombre, descripcion, fecha_inicio)
    
    if CRUDProyecto.agregar(p):
        print("Proyecto registrado.")
    else:
        print("Error al registrar proyecto.")
    input("Presione Enter para continuar...")

def mostrar_proyectos():
    proys = CRUDProyecto.mostrartodos()
    if not proys:
        print("No hay proyectos.")
        input("Presione Enter para continuar...")
        return
    print("\nID (User ID) | Nombre | Descripción | Fecha de inicio")
    print("-" * 60)
    for p in proys:
        print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]}")
    input("Presione Enter para continuar...")

def modificar_proyecto():
    try:
        proy_id = int(input("ID (user_id) del proyecto a modificar: "))
    except ValueError:
        print("ID debe ser numérico.")
        input("Presione Enter para continuar...")
        return
    
    actual = CRUDProyecto.consultarparticular(proy_id)
    if not actual:
        print("Proyecto no encontrado.")
        input("Presione Enter para continuar...")
        return
    
    print("Deje un campo vacío para conservar su valor actual.")
    nombre = input(f"Nombre [{actual[1]}]: ").strip() or actual[1]
    descripcion = input(f"Descripción [{actual[2]}]: ").strip() or actual[2]
    fecha = input(f"Fecha [{actual[3]}]: ").strip() or actual[3]

    p = Proyecto(nombre, descripcion, fecha, proy_id)
    
    if CRUDProyecto.editar(p):
        print("Proyecto modificado.")
    else:
        print("Error al modificar.")
    input("Presione Enter para continuar...")

def eliminar_proyecto():
    try:
        proy_id = int(input("ID (user_id) del proyecto a eliminar: "))
    except ValueError:
        print("El ID debe ser entero.")
        input("Presione Enter para continuar...")
        return
    if CRUDProyecto.eliminar(proy_id):
        print("Proyecto eliminado.")
    else:
        print("No se pudo eliminar.")
    input("Presione Enter para continuar...")


# ==========================================
# CRUD TIEMPO (PK: user_id)
# ==========================================

def ingresar_tiempo():
    os.system('cls')
    print("\n--- REGISTRAR TIEMPO ---")
    try:
        emp_id = int(input("ID numérico del Empleado: "))
        proy_id = int(input("ID del Proyecto (user_id): "))
        fecha = input("Fecha (YYYY-MM-DD): ")
        horas = float(input("Horas Trabajadas: "))
    except ValueError:
        print("Error: IDs deben ser enteros y horas en formato decimal.")
        input("Presione Enter para continuar...")
        return
    descripcion = input("Descripción de tarea: ")

    t = RegistroTiempo(emp_id, proy_id, fecha, horas, descripcion)
    
    if CRUDTiempo.agregar(t):
        print("Tiempo registrado correctamente.")
    else:
        print("Error al registrar.")
    input("Presione Enter para continuar...")

def mostrar_tiempos():
    tiempos = CRUDTiempo.mostrartodos()
    if not tiempos:
        print("No hay registros de tiempo.")
        input("Presione Enter para continuar...")
        return
    print("\nReg. ID | ID Emp | ID Proy | Fecha | Horas | Descripción")
    print("-" * 80)
    for t in tiempos:
        print(f"{t[0]} | {t[1]} | {t[2]} | {t[3]} | {t[4]} | {t[5]}")
    input("Presione Enter para continuar...")

def modificar_tiempo():
    try:
        t_id = int(input("ID del Registro de Tiempo (user_id) a modificar: "))
    except ValueError:
        print("El ID debe ser entero.")
        input("Presione Enter para continuar...")
        return
    
    actual = CRUDTiempo.consultarparticular(t_id)
    if not actual:
        print("Registro no encontrado.")
        input("Presione Enter para continuar...")
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
        input("Presione Enter para continuar...")
        return
    descripcion = input(f"Descripción [{actual[5]}]: ").strip() or actual[5]

    t = RegistroTiempo(emp_id, proy_id, fecha, horas, descripcion, t_id)
    
    if CRUDTiempo.editar(t):
        print("Registro de tiempo modificado.")
    else:
        print("Error al modificar.")
    input("Presione Enter para continuar...")

def eliminar_tiempo():
    try:
        t_id = int(input("ID del registro a eliminar: "))
    except ValueError:
        print("El ID debe ser entero.")
        input("Presione Enter para continuar...")
        return
    if CRUDTiempo.eliminar(t_id):
        print("Registro eliminado.")
    else:
        print("No se pudo eliminar.")
    input("Presione Enter para continuar...")


# ==========================================
# CRUD ASIGNACIÓN (PK: empleado_id)
# ==========================================

def ingresar_asignacion():
    os.system('cls')
    print("\n--- ASIGNAR EMPLEADO A PROYECTO ---")
    try:
        emp_id = int(input("ID numérico del Empleado (PK de la tabla): "))
        proy_id = int(input("ID del Proyecto: "))
    except ValueError:
        print("Los IDs deben ser números enteros.")
        input("Presione Enter para continuar...")
        return
    
    rol = input("Rol a desempeñar: ")

    # Constructor idéntico al diagrama (no pide fecha)
    a = AsignacionEmp(emp_id, proy_id, rol)
    
    if CRUDAsignacion_emp.agregar(a):
        print("Asignación completada.")
    else:
        print("Error al asignar.")
    input("Presione Enter para continuar...")

def mostrar_asignaciones():
    asig = CRUDAsignacion_emp.mostrartodos()
    if not asig:
        print("No hay asignaciones registradas.")
        input("Presione Enter para continuar...")
        return
    
    print("\nID Emp. | ID Proy. | Rol")
    print("-" * 50)
    for a in asig:
        # Imprime los 3 datos correspondientes a empleado_id, proyecto_id y rol
        print(f"{a[0]} | {a[1]} | {a[2]}")
        
    input("Presione Enter para continuar...")

def modificar_asignacion():
    print("\n--- MODIFICAR ASIGNACIÓN ---")
    try:
        emp_id = int(input("ID del Empleado asignado: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        input("Presione Enter para continuar...")
        return

    # Nota: la BD original tiene empleado_id como PK
    actual = CRUDAsignacion_emp.consultarparticular(emp_id)
    if not actual:
        print("No se encontró esa asignación.")
        input("Presione Enter para continuar...")
        return
    
    try:
        proy_txt = input(f"Nuevo ID Proyecto [{actual[1]}]: ").strip()
        proy_id = int(proy_txt) if proy_txt else actual[1]
    except ValueError:
        print("El ID debe ser numérico.")
        input("Presione Enter para continuar...")
        return
        
    rol = input(f"Nuevo Rol [{actual[2]}]: ").strip() or actual[2]

    a = AsignacionEmp(emp_id, proy_id, rol)
    
    if CRUDAsignacion_emp.editar(a):
        print("Asignación modificada.")
    else:
        print("Error al modificar.")
    input("Presione Enter para continuar...")

def eliminar_asignacion():
    print("\n--- ELIMINAR ASIGNACIÓN ---")
    try:
        emp_id = int(input("ID del Empleado a desvincular: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        input("Presione Enter para continuar...")
        return
    
    if CRUDAsignacion_emp.eliminar(emp_id):
        print("Asignación eliminada correctamente.")
    else:
        print("No se pudo eliminar.")
    input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()