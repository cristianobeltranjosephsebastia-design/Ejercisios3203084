class Persona:
    def __init__(self, Nombre, Edad):
        self.Nombre = Nombre
        self.Edad = Edad

    def __repr__(self):
        return f"Persona(Nombre:'{self.Nombre}', Edad:{self.Edad})"


Persona1 = Persona("Pablo", "30")

print(Persona1)
print(repr(Persona1))


