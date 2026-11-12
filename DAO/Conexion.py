import pymysql

class Conexion:
    def __init__(self, host, user, password, db):
        try:
            self.db = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=db
            )
            self.cursor = self.db.cursor()
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")


    def ejecuta_query(self, sql, valores=None):
        try:
            if valores:
                self.cursor.execute(sql, valores)
            else:
                self.cursor.execute(sql)
            return self.cursor
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")
            return None

    def desconectar(self):
        if self.db:
            self.db.close()

    def commit(self):
        if self.db:
            self.db.commit()

    def rollback(self):
        if self.db:
            self.db.rollback()

    def obtenerUsuario(self, username):
        try:
            sql = "SELECT user_id, username, password_hash, nombre, apellidos, correo, tipo_usuario FROM usuario WHERE username = %s"
            self.cursor.execute(sql, (username,))
            return self.cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
            return None

    def agregarUsuario(self, username, password_hash, nombre, apellidos, correo, tipo_usuario):
        try:
            sql = "INSERT INTO usuario (username, password_hash, nombre, apellidos, correo, tipo_usuario) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (username, password_hash, nombre, apellidos, correo, tipo_usuario)
            self.cursor.execute(sql, valores)
            self.commit()
            return True
        except Exception as e:
            print(f"Error al agregar el usuario: {e}")
            self.rollback()
            return False
