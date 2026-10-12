from DTO.Persona import Persona

class Empleado(Persona):
    def __init__(self, run, nombre, direccion, telefono, correo, fecha_inicio, salario, departamento_id, user_id=None):
        super().__init__(run, nombre, direccion, telefono, correo, user_id)
        self.fecha_inicio = fecha_inicio
        self.salario = salario
        self.departamento_id = departamento_id

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_salario(self):
        return self.salario

    def get_departamento_id(self):
        return self.departamento_id

    def info(self):
        return f"Empleado: {self.nombre}, RUN: {self.run}, Salario: {self.salario}, Depto: {self.departamento_id}"

    def __str__(self):
        return f"{self.run} - {self.nombre} (Depto: {self.departamento_id})"