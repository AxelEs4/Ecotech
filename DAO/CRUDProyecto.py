from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

# Creación
def agregar(p):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """INSERT INTO proyecto (nombre, descripcion, fecha_inicio) 
                 VALUES (%s, %s, %s)"""
        valores = (p.nombre, p.descripcion, p.fecha_inicio)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el INSERT de proyecto.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error al agregar proyecto: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(p):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """UPDATE proyecto 
                 SET nombre=%s, descripcion=%s, fecha_inicio=%s 
                 WHERE proyecto_id=%s"""
        proy_id = getattr(p, 'proyecto_id', getattr(p, 'id', None))
        valores = (p.nombre, p.descripcion, p.fecha_inicio, proy_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el UPDATE de proyecto.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error al modificar proyecto: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def eliminar(id_proyecto):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = "DELETE FROM proyecto WHERE proyecto_id=%s"
        con.ejecuta_query(sql, (id_proyecto,))
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