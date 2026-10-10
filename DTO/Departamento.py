class Departamento:
    def __init__(self, nombre, gerente_emp_id=None, descripcion=None):
        self.nombre = nombre
        self.gerente_emp_id = gerente_emp_id
        self.descripcion = descripcion
        self.user_id = None