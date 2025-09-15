
class Agenda:
    def __init__(self, Nombre, Telefono):
        self.Nombre = Nombre
        self.Telefono = Telefono
        self.elementos = []

    def agregar_contactos(self, contacto):
        self.elementos.append(contacto)

    def mostrar_contactos(self):
        print(f"Es {self.Nombre}, {self.Telefono}, {self.elementos}")    

Persona1 = Agenda ("Sebastian", "30059229573", )
Persona1.agregar_contactos("Persona1")

Persona1.mostrar_contactos()