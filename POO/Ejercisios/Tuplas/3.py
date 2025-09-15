class Juegos_Moviles:
    def __init__(self, Nombre, Ratio):
        self.Nombre = Nombre
        self.Ratio = Ratio

    def __repr__(self):
        return f"Persona(Nombre:'{self.Nombre}', Puntuacion: {self.Ratio})"


Juego1 = Juegos_Moviles ("Free fire", "4.5")
Juego2 = Juegos_Moviles ("Clash Royales", "4.4")


print(Juego1)
print(Juego2)

