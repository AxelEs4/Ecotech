from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

def agregar(d):
    con = None
    try:
        con = Conexion(host, user, password, db)
        # El ID se genera solo. Si no hay gerente, enviamos None
        gerente = d.gerente_empleado_id if d.gerente_empleado_id != 0 else None
        
        sql = "INSERT INTO departamento (nombre, descripcion, gerente_emp_id) VALUES (%s, %s, %s)"
        cursor = con.ejecuta_query(sql, (d.nombre, d.descripcion, gerente))
        if cursor is None: raise RuntimeError("Error en INSERT.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(d):
    con = None
    try:
        con = Conexion(host, user, password, db)
        gerente = d.gerente_empleado_id if d.gerente_empleado_id != 0 else None
        
        sql = "UPDATE departamento SET descripcion=%s, gerente_emp_id=%s WHERE nombre=%s"
        cursor = con.ejecuta_query(sql, (d.descripcion, gerente, d.nombre))
        if cursor is None: raise RuntimeError("Error en UPDATE.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def eliminar(nombre):
    con = None
    try:
        con = Conexion(host, user, password, db)
        con.ejecuta_query("DELETE FROM departamento WHERE nombre=%s", (nombre,))
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
        sql = "SELECT nombre, descripcion, IFNULL(gerente_emp_id, 0), departamento_id FROM departamento"
        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []
    except Exception:
        return []
    finally:
        if con: con.desconectar()

def consultarparticular(nombre):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT nombre, descripcion, IFNULL(gerente_emp_id, 0), departamento_id FROM departamento WHERE nombre = %s"
        cursor = con.ejecuta_query(sql, (nombre,))
        return cursor.fetchone() if cursor else None
    except Exception:
        return None
    finally:
        if con: con.desconectar()