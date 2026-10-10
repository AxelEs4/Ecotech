from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db="empresa"

# Creación registro de tiempo
def agregar(registro):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "INSERT INTO RegistroTiempo (empleado_id, proyecto_id, fecha, horas, descripcion) VALUES (%s, %s, %s, %s, %s)"
        valores = (registro.empleado_id, registro.proyecto_id, registro.fecha, registro.horas, registro.descripcion)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el INSERT de registro de tiempo.")
        con.commit()

        return True

    except Exception as e:
        print(f"Error al agregar registro de tiempo: {e}")
        if con:
            con.rollback()
        return False

    finally:
        if con:
            con.desconectar()

def mostrarTodos():
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT * FROM RegistroTiempo"
        
        cursor = con.ejecuta_query(sql, ())
        if cursor is None:
            raise RuntimeError("No se pudo ejecutar el SELECT general.")
            
        # Dependiendo de tu librería, aquí recuperas los datos del cursor
        resultados = cursor.fetchall() 
        return resultados

    except Exception as e:
        print(f"Error al mostrar los registros de tiempo: {e}")
        return []

    finally:
        if con:
            con.desconectar()

def consultaPorEmpleado(empleado_id):
    con = None
    try:
        con = Conexion(host, user, password, db)

        sql = "SELECT * FROM RegistroTiempo WHERE empleado_id = %s"
        valores = (empleado_id,)

        cursor = con.ejecuta_query(sql, valores)
        if cursor is None:
            raise RuntimeError(f"No se pudo ejecutar el SELECT para el empleado {empleado_id}.")
            
        resultados = cursor.fetchall()
        return resultados

    except Exception as e:
        print(f"Error al consultar los registros del empleado: {e}")
        return []

    finally:
        if con:
            con.desconectar()