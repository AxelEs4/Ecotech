from DAO.Conexion import Conexion
import bcrypt

host = "localhost"
user = "userempresa"
db_password = "Pimienta12."
db = "ecotech"

class Usuario:
    def __init__(self, user_id, username, password, nombre, apellidos, correo, tipo_usuario):
        self.user_id = user_id
        self.user_name = username
        self.password_hash = password
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.tipo_usuario = tipo_usuario

    @staticmethod
    def login(username,password):
                con = None
                try:
                    con = Conexion(host, user, db_password, db)
                    usuario_data= con.obtenerUsuario(username)

                    if usuario_data:
                        hashed_password = usuario_data[2].encode('utf-8')

                        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                            return Usuario(
                                user_id=usuario_data[0],
                                username=usuario_data[1],
                                password=usuario_data[2],
                                nombre=usuario_data[3],
                                apellidos=usuario_data[4],
                                correo=usuario_data[5],
                                tipo_usuario=usuario_data[6]
                            )
                    return None

                except Exception as e:
                    print(f"Error al intentar iniciar sesión: {e}")
                    return None

                finally:
                    if con:
                        con.desconectar()

    @staticmethod
    def register(username, password, nombre, apellidos, email, tipo_usuario):
        con = None
        try:
            roles = {
                "admin": "Administrador",
                "administrador": "Administrador",
                "usuario": "Operador",
                "operador": "Operador",
            }
            tipo_usuario = roles.get(tipo_usuario.strip().casefold())
            if tipo_usuario is None:
                raise ValueError(
                    "El tipo de usuario debe ser Administrador o Operador."
                )

            hashed_password = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            con = Conexion(host, user, db_password, db)

            exito = con.agregarUsuario(
                username=username,
                password_hash=hashed_password,
                nombre=nombre,
                apellidos=apellidos,
                correo=email,
                tipo_usuario=tipo_usuario
            )

            return exito

        except Exception as e:
            print(f"Error al intentar registrar usuario: {e}")
            return False

        finally:
            if con:
                con.desconectar()