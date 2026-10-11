from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

# Creación
def agregar(e):
    con = None
    try:
        con = Conexion(host, user, password, db)
        # No se envía empleado_id porque es AUTO_INCREMENT
        sql = """INSERT INTO empleado (run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el INSERT de empleado.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error al agregar empleado: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(e):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """UPDATE empleado 
                 SET run=%s, nombre=%s, direccion=%s, telefono=%s, correo=%s, fecha_inicio=%s, salario=%s, departamento_id=%s 
                 WHERE empleado_id=%s"""
        
        emp_id = getattr(e, 'empleado_id', getattr(e, 'id', None))
        valores = (e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id, emp_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el UPDATE de empleado.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error al modificar empleado: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def eliminar(id_empleado):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM empleado WHERE empleado_id=%s"
        con.ejecuta_query(sql, (id_empleado,))
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
        sql = """SELECT e.empleado_id, e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, d.nombre 
                 FROM empleado e LEFT JOIN departamento d ON e.departamento_id = d.departamento_id"""
        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []
    except Exception:
        return []
    finally:
        if con: con.desconectar()


# Consulta particular
def consultarparticular(id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """SELECT USER_ID, run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id 
                 FROM EMPLEADO WHERE USER_ID = %s"""
        cursor = con.ejecuta_query(sql, (id,))

        return cursor.fetchone() if cursor else None

    except Exception:
        return None

    finally:
        if con:
            con.desconectar()


