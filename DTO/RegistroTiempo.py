class RegistroTiempo:
    def __init__(self, empleado_id, proyecto_id, fecha, horas, descripcion, user_id=None):
        self.user_id = user_id
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion