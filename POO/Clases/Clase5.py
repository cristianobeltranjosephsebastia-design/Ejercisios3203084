class personas:
    def __new__(cls, Nombre, Edad):
        return super(). __new__(cls)
    
    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad = Edad

    def __del__(self):
        print(f"Ha sido eliminado {self.Nombre}")

Ana = personas ("Ana", 30)
Carlos = personas ("Carlos", 47)

print(f'{Ana.Nombre}, {Ana.Edad}, {Carlos.Nombre}, {Carlos.Edad}')