class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio, user_id=None):
        self.user_id = user_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio