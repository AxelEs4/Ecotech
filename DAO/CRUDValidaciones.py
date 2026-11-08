import re
from datetime import datetime
from DAO.Conexion import Conexion

host = "localhost"
user = "userempresa"
password = "Pimienta12."
db = "ecotech"

def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def existe_empleado(run):
    con = None
    try:
        con = Conexion(host, user, password, db)
        cursor = con.ejecuta_query("SELECT run FROM empleado WHERE run = %s", (run,))
        return cursor.fetchone() is not None
    except:
        return False
    finally:
        if con: con.desconectar()

def existe_empleado_id(empleado_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        cursor = con.ejecuta_query(
            "SELECT empleado_id FROM empleado WHERE empleado_id = %s",
            (empleado_id,)
        )
        if cursor is None:
            return None
        return cursor.fetchone() is not None
    except Exception as ex:
        print(f"Error al verificar el ID del empleado: {ex}")
        return None
    finally:
        if con: con.desconectar()

def existe_proyecto(user_id):
    con = None
    try:
        con = Conexion(host, user, password, db)
        cursor = con.ejecuta_query("SELECT user_id FROM proyecto WHERE user_id = %s", (user_id,))
        return cursor.fetchone() is not None
    except:
        return False
    finally:
        if con: con.desconectar()

def existe_departamento(nombre):
    con = None
    try:
        con = Conexion(host, user, password, db)
        cursor = con.ejecuta_query("SELECT nombre FROM departamento WHERE nombre = %s", (nombre,))
        return cursor.fetchone() is not None
    except:
        return False
    finally:
        if con: con.desconectar()

def validar_run(run):
    # Validar formato RUN (sin puntos, con guion y dígito verificador)
    if not re.match(r'^\d{7,8}-[0-9kK]$', run):
        return False

    # Separar el número y el dígito verificador
    numero, dv = run.split('-')
    numero = int(numero)
    dv = dv.lower()

    # Calcular el dígito verificador esperado
    suma = 0
    multiplicador = 2
    while numero > 0:
        suma += (numero % 10) * multiplicador
        numero //= 10
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    dv_calculado = 'k' if resto == 1 else str(11 - resto) if resto != 0 else '0'

    return dv == dv_calculado

def validar_correo(correo):
    # Validar formato de correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None