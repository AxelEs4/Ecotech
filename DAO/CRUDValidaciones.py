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