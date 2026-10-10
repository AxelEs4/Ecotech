from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "empresa"

# Creación
def agregar(e):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """INSERT INTO EMPLEADO (run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        valores = (e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el INSERT de empleado; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as ex:
        print(f"Error al agregar empleado: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()


# Edición
def editar(e):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """UPDATE EMPLEADO 
                 SET run=%s, nombre=%s, direccion=%s, telefono=%s, correo=%s, fecha_inicio=%s, salario=%s, departamento_id=%s 
                 WHERE USER_ID=%s"""
        emp_id = getattr(e, 'user_id', getattr(e, 'id', None))
        valores = (e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, e.departamento_id, emp_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el UPDATE del empleado; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as ex:
        print(f"Error al modificar empleado: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()


# Eliminación
def eliminar(id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "DELETE FROM EMPLEADO WHERE USER_ID=%s"

        con.ejecuta_query(sql, (id,))
        con.commit()

        return True

    except Exception:
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

        sql = """SELECT e.USER_ID, e.run, e.nombre, e.direccion, e.telefono, e.correo, e.fecha_inicio, e.salario, d.nombre 
                 FROM EMPLEADO e LEFT JOIN DEPARTAMENTO d ON e.departamento_id = d.id"""

        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []

    except Exception:
        return []

    finally:
        if con:
            con.desconectar()


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


def mostrardepartamentos():
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT id, nombre FROM DEPARTAMENTO"

        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []

    except Exception:
        return []

    finally:
        if con:
            con.desconectar()