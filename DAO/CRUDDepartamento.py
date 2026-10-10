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

        sql = "INSERT INTO DEPARTAMENTO (user_id, nombre, gerente_empleado_id, descripcion) VALUES (%s, %s, %s, %s)"
        valores = (c.user_id, c.nombre, c.gerente_empleado_id, c.descripcion)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el INSERT del departamento; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as e:
        print(f"Error al agregar departamento: {e}")
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

        sql = """SELECT c.nombre, c.gerente_empleado_id, c.descripcion
        FROM DEPARTAMENTO c"""

        cursor = con.ejecuta_query(sql)
        return cursor.fetchall()

    except Exception:
        return []

    finally:
        if con:
            con.desconectar()


#CONSULTA PARTICULAR
def consultarparticular(id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT c.nombre, c.gerente_empleado_id, c.descripcion FROM DEPARTAMENTO c WHERE c.departamento_id = %s"
        valores = (id,)

        cursor = con.ejecuta_query(sql, valores)
        return cursor.fetchone()

    except Exception as e:
        print(f"Error al consultar departamento: {e}")
        return None

    finally:
        if con:
            con.desconectar()


#Edicion
def editar(c):
    con=None
    try:
        con= Conexion(host, user, password, db)

        sql = "UPDATE DEPARTAMENTO SET nombre=%s, gerente_empleado_id=%s, descripcion=%s WHERE departamento_id=%s"
        valores = (c.nombre, c.gerente_empleado_id, c.descripcion, c.departamento_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el UPDATE del departamento; revisa el error de MySQL mostrado arriba.")
        con.commit()

        return True

    except Exception as e:
        print(f"Error al modificar departamento: {e}")
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

        sql = "DELETE FROM DEPARTAMENTO WHERE departamento_id=%s"
        

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