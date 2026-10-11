class Departamento:
    def __init__(self, departamento_id, nombre, descripcion=None, gerente_emp_id=None):
        self.departamento_id = departamento_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.gerente_emp_id = gerente_emp_id