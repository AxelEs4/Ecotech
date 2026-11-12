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

def eliminar(nombre, accion_empleados=None, departamento_destino_id=None):
    con = None
    try:
        con = Conexion(host, user, password, db)
        cursor = con.ejecuta_query(
            "SELECT departamento_id FROM departamento WHERE nombre=%s FOR UPDATE",
            (nombre,)
        )
        if cursor is None:
            raise RuntimeError("No se pudo consultar el departamento.")
        departamento = cursor.fetchone()
        if departamento is None:
            return False
        departamento_id = departamento[0]

        if accion_empleados == "eliminar":
            cursor = con.ejecuta_query(
                "DELETE FROM empleado WHERE departamento_id=%s",
                (departamento_id,)
            )
            if cursor is None:
                raise RuntimeError("No se pudieron eliminar los empleados del departamento.")
        elif accion_empleados == "reasignar":
            if departamento_destino_id is None or departamento_destino_id == departamento_id:
                raise ValueError("Debe seleccionar otro departamento como destino.")
            cursor = con.ejecuta_query(
                "UPDATE empleado SET departamento_id=%s WHERE departamento_id=%s",
                (departamento_destino_id, departamento_id)
            )
            if cursor is None:
                raise RuntimeError("No se pudieron reasignar los empleados.")
        elif accion_empleados is not None:
            raise ValueError("Acción de empleados no válida.")

        cursor = con.ejecuta_query("DELETE FROM departamento WHERE departamento_id=%s", (departamento_id,))
        if cursor is None:
            raise RuntimeError("No se pudo eliminar el departamento.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error al eliminar departamento: {ex}")
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