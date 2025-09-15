class Juegos_Pc:
    def __init__(self, Nombre, Plataforma):
        self.Nombre = Nombre
        self.Plataforma = Plataforma

    def __repr__(self):
        return f"Persona(Nombre:'{self.Nombre}', Plataforma: {self.Plataforma})"


Juego1 = Juegos_Pc ("Hollow Knight: Silksong", "Steam")
Juego2 = Juegos_Pc ("Valorant", "Riot/EA")


print(Juego1)
print(Juego2)

