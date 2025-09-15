class Empresa:
    def __init__(self, Empleados, Instalaciones, Nombre, Jefe):
        self.Empleados = Empleados
        self.Instalaciones = Instalaciones
        self.Nombre = Nombre
        self.Jefe = Jefe

Empresa1 = Empresa("100", "5", "AgroCol", "Parra")

print(Empresa1.Empleados, Empresa1.Instalaciones, Empresa1.Nombre, Empresa1.Jefe)