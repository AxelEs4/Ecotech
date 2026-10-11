from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db="ecotech"

#Creación
def agregar(a):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """INSERT INTO asignacion_emp (empleado_id, proyecto_id, rol, fecha_inicio) 
                 VALUES (%s, %s, %s, %s)"""
        valores = (a.empleado_id, a.proyecto_id, a.rol, a.fecha_inicio)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el INSERT de asignación.")
        con.commit()
        return True

    except Exception as ex:
        print(f"Error al agregar asignación: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# Edición (Requiere conocer qué empleado y en qué proyecto se va a actualizar)
def editar(a):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """UPDATE asignacion_emp 
                 SET rol=%s, fecha_inicio=%s 
                 WHERE empleado_id=%s AND proyecto_id=%s"""
        
        valores = (a.rol, a.fecha_inicio, a.empleado_id, a.proyecto_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el UPDATE de asignación.")
        con.commit()
        return True

    except Exception as ex:
        print(f"Error al modificar asignación: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# Eliminación (Se necesitan ambos IDs para no borrar de más)
def eliminar(empleado_id, proyecto_id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "DELETE FROM asignacion_emp WHERE empleado_id=%s AND proyecto_id=%s"

        con.ejecuta_query(sql, (empleado_id, proyecto_id))
        con.commit()
        return True

    except Exception as ex:
        print(f"Error al eliminar asignación: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# Mostrar todos
def mostrartodos():
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """SELECT a.empleado_id, e.nombre AS empleado, a.proyecto_id, p.nombre AS proyecto, a.rol, a.fecha_inicio 
                 FROM asignacion_emp a
                 INNER JOIN empleado e ON a.empleado_id = e.empleado_id
                 INNER JOIN proyecto p ON a.proyecto_id = p.proyecto_id"""

        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []

    except Exception as ex:
        print(f"Error al consultar asignaciones: {ex}")
        return []

    finally:
        if con:
            con.desconectar()

# Consulta particular
def consultarparticular(empleado_id, proyecto_id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """SELECT empleado_id, proyecto_id, rol, fecha_inicio 
                 FROM asignacion_emp 
                 WHERE empleado_id = %s AND proyecto_id = %s"""
        cursor = con.ejecuta_query(sql, (empleado_id, proyecto_id))

        return cursor.fetchone() if cursor else None

    except Exception as ex:
        print(f"Error al consultar la asignación específica: {ex}")
        return None

    finally:
        if con:
            con.desconectar()