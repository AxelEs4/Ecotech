from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db="ecotech"


#Creación
def agregar(d):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """INSERT INTO departamento (nombre, descripcion, gerente_emp_id) 
                 VALUES (%s, %s, %s)"""
        valores = (d.nombre, d.descripcion, d.gerente_emp_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el INSERT de departamento.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error al agregar departamento: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def editar(d):
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """UPDATE departamento 
                 SET nombre=%s, descripcion=%s, gerente_emp_id=%s 
                 WHERE departamento_id=%s"""
        depto_id = getattr(d, 'departamento_id', getattr(d, 'id', None))
        valores = (d.nombre, d.descripcion, d.gerente_emp_id, depto_id)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("Error al ejecutar el UPDATE de departamento.")
        con.commit()
        return True
    except Exception as ex:
        print(f"Error al modificar departamento: {ex}")
        if con: con.rollback()
        return False
    finally:
        if con: con.desconectar()

def mostrartodos():
    con = None
    try:
        con = Conexion(host, user, password, db)
        sql = """SELECT d.departamento_id, d.nombre, d.descripcion, d.gerente_emp_id, e.nombre AS nombre_gerente 
                 FROM departamento d 
                 LEFT JOIN empleado e ON d.gerente_emp_id = e.empleado_id"""
        cursor = con.ejecuta_query(sql)
        return cursor.fetchall() if cursor else []
    except Exception:
        return []
    finally:
        if con: con.desconectar()
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