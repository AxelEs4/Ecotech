class RegistroTiempo:
    def __init__(self, empleado_id, proyecto_id, fecha, horas, descripcion):
        # Atributos protegidos/privados
        self._empleado_id = empleado_id
        self._proyecto_id = proyecto_id
        self._fecha = fecha
        self._horas = horas
        self._descripcion = descripcion