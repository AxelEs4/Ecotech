from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

def agregar(t):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO tiempo (empleado_id, proyecto_id, fecha, horas, descripcion) VALUES (%s, %s, %s, %s, %s)"
        cursor = con.ejecuta_query(sql, (t.empleado_id, t.proyecto_id, t.fecha, t.horas, t.descripcion))
        if cursor is None: raise RuntimeError("Error en INSERT.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(t):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "UPDATE tiempo SET empleado_id=%s, proyecto_id=%s, fecha=%s, horas=%s, descripcion=%s WHERE tiempo_id=%s"
        cursor = con.ejecuta_query(sql, (t.empleado_id, t.proyecto_id, t.fecha, t.horas, t.descripcion, t.user_id))
        if cursor is None: raise RuntimeError("Error en UPDATE.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def eliminar(tiempo_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        con.ejecuta_query("DELETE FROM tiempo WHERE tiempo_id=%s", (tiempo_id,))
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
        sql = "SELECT tiempo_id, empleado_id, proyecto_id, fecha, horas, descripcion FROM tiempo"
        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []
    except Exception:
        return []
    finally:
        if con: con.desconectar()

def consultarparticular(tiempo_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT tiempo_id, empleado_id, proyecto_id, fecha, horas, descripcion FROM tiempo WHERE tiempo_id = %s"
        cursor = con.ejecuta_query(sql, (tiempo_id,))
        return cursor.fetchone() if cursor else None
    except Exception:
        return None
    finally:
        if con: con.desconectar()