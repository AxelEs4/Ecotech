class Departamento:
    def __init__(self, nombre, gerente_empleado_id, descripcion, user_id=None):
        self.user_id = user_id
        self.nombre = nombre
        self.gerente_empleado_id = gerente_empleado_id
        self.descripcion = descripcion