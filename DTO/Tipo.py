class Tipo_Empleado:
    def __init__(self,codigo,nombre):
        self.id=codigo
        self.nombre=nombre
        
    def __str__(self) -> str:
        return f"Cod: {self.id} - {self.nombre}"
