class Personas:
    def __init__(self, Nombre, Apellido):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.elementos = []

    def agregar_elementos(self, elemento):
        self.elementos.append(elemento)

    def mostrar_elementos(self):
        print(f"Es {self.Nombre}, {self.Apellido}, {self.elementos}")    

Persona1 = Personas ("Sebastian", "Cristiano", )
Persona1.agregar_elementos("Persona1")
Persona1.agregar_elementos("Persona2")

Persona1.mostrar_elementos()