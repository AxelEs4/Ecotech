class AsignacionEmp:
    def __init__(self, empleado_id, proyecto_id, rol, asignacion_id=None):
        self.asignacion_id = asignacion_id
        self.empleado_id = empleado_id
        self.proyecto_id = proyecto_id
        self.rol = rol