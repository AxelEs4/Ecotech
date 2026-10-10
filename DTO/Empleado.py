from .Persona import Persona


class Empleado(Persona):
    def __init__(self, user_id, departamento_id, run, nombre, direccion, telefono, correo, fecha_inicio, salario):
        super().__init__(user_id, run, nombre, direccion, telefono, correo)
        self.departamento_id = departamento_id
        self.fecha_inicio = fecha_inicio
        self.salario = salario