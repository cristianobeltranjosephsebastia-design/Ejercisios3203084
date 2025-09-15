class Juegos:
    def __init__(self, Nombre, Plataforma):
        self.Nombre = Nombre
        self.Plataforma = Plataforma

    def presentarse(self):
        return f"Hola, este es {self.Nombre} y esta en {self.Plataforma} "


Juego = [
    Juegos("Valorant", "Steam"),
    Juegos("Peak", "Steam"),
    Juegos("Warzone", "Steam")
]


for Juegos in Juego:
    print(Juegos.presentarse())

