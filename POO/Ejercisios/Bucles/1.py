class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


personas = [
    Persona("Sebastian", 30),
    Persona("Luis", 25),
    Persona("Pablo", 35)
]


for persona in personas:
    print(persona.presentarse())

