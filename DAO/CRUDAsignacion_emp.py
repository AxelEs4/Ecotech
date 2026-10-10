from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db="empresa"

#Creación
def agregar(c):
    con=None
    try:
        con= Conexion(host, user, password, db)

        sql = "INSERT INTO DEPARTAMENTO (empleado_id, asignacion_id, proyecto_id, rol) VALUES (%s, %s, %s, %s)"
        valores = (c.empleado_id, c.asignacion_id, c.proyecto_id, c.rol)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el INSERT de cliente; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as e:
        print(f"Error al agregar cliente: {e}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()


#Mostrar
def mostrartodos():
    con=None
    try:
        con= Conexion(host, user, password, db)

        sql = """SELECT c.empleado_id, c.asignacion_id, c.proyecto_id, c.rol
        FROM ASIGNACION_EMP c"""

        cursor = con.ejecuta_query(sql)
        return cursor.fetchall()

    except Exception:
        return []

    finally:
        if con:
            con.desconectar()


#cONSULTA PARTICULAR
def consultarparticular(id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT empleado_id, asignacion_id, proyecto_id, rol FROM ASIGNACION_EMP WHERE empleado_id = %s"
        cursor = con.ejecuta_query(sql, (id,))

        return cursor.fetchone() if cursor else None

    except Exception:
        return None

    finally:
        if con:
            con.desconectar()


#Edicion
def editar(c):
    con=None
    try:
        con= Conexion(host, user, password, db)

        sql = "UPDATE ASIGNACION_EMP SET empleado_id=%s, asignacion_id=%s, proyecto_id=%s, rol=%s WHERE empleado_id=%s AND asignacion_id=%s AND proyecto_id=%s"
        valores = (c.empleado_id, c.asignacion_id, c.proyecto_id, c.rol)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el UPDATE de la asignación; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as e:
        print(f"Error al modificar al empleado: {e}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()


#Eliminacion
def eliminar(id):
    con=None
    try:
        con= Conexion(host, user, password, db)

        sql = "DELETE FROM ASIGNACION_EMP WHERE empleado_id=%s"
        

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