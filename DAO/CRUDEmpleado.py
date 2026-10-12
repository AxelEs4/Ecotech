from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

def agregar(e):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """INSERT INTO empleado (run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id)
        cursor = con.ejecuta_query(sql, valores)
        if cursor is None: raise RuntimeError("Error en INSERT.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(e):
    con = None
    try:
        con = Conexion(host, user, password, db)
        # Editamos buscando por el RUN (que es único)
        sql = """UPDATE empleado 
                 SET nombre=%s, direccion=%s, telefono=%s, correo=%s, fecha_inicio=%s, salario=%s, departamento_id=%s 
                 WHERE run=%s"""
        valores = (e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id, e.run)
        cursor = con.ejecuta_query(sql, valores)
        if cursor is None: raise RuntimeError("Error en UPDATE.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def eliminar(run):
    con = None
    try:
        con = Conexion(host, user, password, db)
        con.ejecuta_query("DELETE FROM empleado WHERE run=%s", (run,))
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
        # Retorna el empleado_id interno al final por si se necesita
        sql = "SELECT run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id, empleado_id FROM empleado"
        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []
    except Exception:
        return []
    finally:
        if con: con.desconectar()

def consultarparticular(run):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "SELECT run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id, empleado_id FROM empleado WHERE run = %s"
        cursor = con.ejecuta_query(sql, (run,))
        return cursor.fetchone() if cursor else None
    except Exception:
        return None
    finally:
        if con: con.desconectar()