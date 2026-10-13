from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

def agregar(a):
    con = None
    try:
        con = Conexion(host, user, password, db)
        # Solo insertamos los 3 datos reales de la BD normalizada
        sql = "INSERT INTO asignacion_emp (empleado_id, proyecto_id, rol) VALUES (%s, %s, %s)"
        cursor = con.ejecuta_query(sql, (a.empleado_id, a.proyecto_id, a.rol))
        
        if cursor is None: raise RuntimeError("Error en INSERT de asignación.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(a):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE asignacion_emp SET rol=%s WHERE empleado_id=%s AND proyecto_id=%s"
        cursor = con.ejecuta_query(sql, (a.rol, a.empleado_id, a.proyecto_id))
        
        if cursor is None: raise RuntimeError("Error en UPDATE de asignación.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def eliminar(empleado_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM asignacion_emp WHERE empleado_id=%s"
        con.ejecuta_query(sql, (empleado_id,))
        con.commit()
        return True
    except Exception:
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def mostrartodos():
    con = None
    try:
        con = Conexion(host, user, password, db)
        # Solo seleccionamos las 3 columnas que existen en el SQL normalizado
        sql = "SELECT empleado_id, proyecto_id, rol FROM asignacion_emp"
        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []
    except Exception:
        return []
    finally:
        if con: con.desconectar()

def consultarparticular(empleado_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT empleado_id, proyecto_id, rol FROM asignacion_emp WHERE empleado_id = %s"
        cursor = con.ejecuta_query(sql, (empleado_id,))
        return cursor.fetchone() if cursor else None
    except Exception:
        return None
    finally:
        if con: con.desconectar()