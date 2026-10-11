from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db="ecotech"

# Creación registro de tiempo
def agregar(t):
    con = None
    try:
        con = Conexion(host, user, password, db)
        
        # No se envía tiempo_id porque es AUTO_INCREMENT
        sql = """INSERT INTO tiempo (empleado_id, proyecto_id, fecha, horas, descripcion) 
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (t.empleado_id, t.proyecto_id, t.fecha, t.horas, t.descripcion)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el INSERT de tiempo.")
        con.commit()
        return True

    except Exception as ex:
        print(f"Error al agregar registro de tiempo: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# Edición
def editar(t):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """UPDATE tiempo 
                 SET empleado_id=%s, proyecto_id=%s, fecha=%s, horas=%s, descripcion=%s 
                 WHERE tiempo_id=%s"""
        
        t_id = getattr(t, 'tiempo_id', getattr(t, 'id', None))
        valores = (t.empleado_id, t.proyecto_id, t.fecha, t.horas, t.descripcion, t_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el UPDATE de tiempo.")
        con.commit()
        return True

    except Exception as ex:
        print(f"Error al modificar registro de tiempo: {ex}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

# Eliminación
def eliminar(tiempo_id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "DELETE FROM tiempo WHERE tiempo_id=%s"

        con.ejecuta_query(sql, (tiempo_id,))
        con.commit()
        return True

    except Exception as ex:
        print(f"Error al eliminar registro de tiempo: {ex}")
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

        sql = """SELECT t.tiempo_id, e.nombre AS empleado, p.nombre AS proyecto, t.fecha, t.horas, t.descripcion 
                 FROM tiempo t 
                 LEFT JOIN empleado e ON t.empleado_id = e.empleado_id 
                 LEFT JOIN proyecto p ON t.proyecto_id = p.proyecto_id"""

        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []

    except Exception as ex:
        print(f"Error al consultar tiempos: {ex}")
        return []

    finally:
        if con:
            con.desconectar()

# Consulta particular
def consultarparticular(tiempo_id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = """SELECT tiempo_id, empleado_id, proyecto_id, fecha, horas, descripcion 
                 FROM tiempo WHERE tiempo_id = %s"""
        cursor = con.ejecuta_query(sql, (tiempo_id,))

        return cursor.fetchone() if cursor else None

    except Exception as ex:
        print(f"Error al consultar el tiempo {tiempo_id}: {ex}")
        return None

    finally:
        if con:
            con.desconectar()