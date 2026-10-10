from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "empresa"

# Creación
def agregar(p):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "INSERT INTO PROYECTO (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
        valores = (p.nombre, p.descripcion, p.fecha_inicio)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el INSERT de proyecto; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as ex:
        print(f"Error al agregar proyecto: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()


# Edición
def editar(p):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "UPDATE PROYECTO SET nombre=%s, descripcion=%s, fecha_inicio=%s WHERE USER_ID=%s"
        proy_id = getattr(p, 'user_id', getattr(p, 'id', None))
        valores = (p.nombre, p.descripcion, p.fecha_inicio, proy_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el UPDATE del proyecto; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as ex:
        print(f"Error al modificar proyecto: {ex}")
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

        sql = "DELETE FROM PROYECTO WHERE USER_ID=%s"

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

        sql = "SELECT USER_ID, nombre, descripcion, fecha_inicio FROM PROYECTO"

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

        sql = "SELECT USER_ID, nombre, descripcion, fecha_inicio FROM PROYECTO WHERE USER_ID = %s"
        cursor = con.ejecuta_query(sql, (id,))

        return cursor.fetchone() if cursor else None

    except Exception:
        return None

    finally:
        if con:
            con.desconectar()