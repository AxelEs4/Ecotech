from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

def agregar(p):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO proyecto (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        cursor = con.ejecuta_query(sql, (p.nombre, p.descripcion, p.fecha_inicio))
        if cursor is None: raise RuntimeError("Error en INSERT.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(p):
    con = None
    try:
        con = Conexion(host, user, password, db)
        # p.user_id almacena el ID del proyecto según el DTO del diagrama
        sql = "UPDATE proyecto SET nombre=%s, descripcion=%s, fecha_inicio=%s WHERE proyecto_id=%s"
        cursor = con.ejecuta_query(sql, (p.nombre, p.descripcion, p.fecha_inicio, p.user_id))
        if cursor is None: raise RuntimeError("Error en UPDATE.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def eliminar(proyecto_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        # El CASCADE borrará automáticamente horas y asignaciones
        con.ejecuta_query("DELETE FROM proyecto WHERE proyecto_id=%s", (proyecto_id,))
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
        sql = "SELECT proyecto_id, nombre, descripcion, fecha_inicio FROM proyecto"
        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []
    except Exception:
        return []
    finally:
        if con: con.desconectar()

def consultarparticular(proyecto_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT proyecto_id, nombre, descripcion, fecha_inicio FROM proyecto WHERE proyecto_id = %s"
        cursor = con.ejecuta_query(sql, (proyecto_id,))
        return cursor.fetchone() if cursor else None
    except Exception:
        return None
    finally:
        if con: con.desconectar()