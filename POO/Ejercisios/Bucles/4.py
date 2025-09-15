class Peliculas:
    def __init__(self, Nombre, Plataforma):
        self.Nombre = Nombre
        self.Plataforma = Plataforma

    def presentarse(self):
        return f"Hola, este es {self.Nombre} y esta en {self.Plataforma} "


Pelicula = [
    Peliculas("Transformers", "Prime video"),
    Peliculas("Interstellar", "HBOMAX"),
    Peliculas("2012", "Netflix")
]


for Peliculas in Pelicula:
    print(Peliculas.presentarse())
