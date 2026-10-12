class Persona:
    def __init__(self, run, nombre, direccion, telefono, correo, user_id=None):
        self.run = run
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.user_id = user_id

    def get_run(self):
        return self.run

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_telefono(self):
        return self.telefono

    def get_correo(self):
        return self.correo

    def get_user_id(self):
        return self.user_id

    def __str__(self):
        return f"{self.run} - {self.nombre}"