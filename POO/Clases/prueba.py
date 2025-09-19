class Personaje:
    def __init__(self, Nombre, Genero, Arma, Clase):
        self.Nombre = Nombre
        self.Genero = Genero
        self.Arma = Arma
        self.Clase = Clase

    def __str__(self):
        return (f"Nombre del personaje: {self.Nombre}, Género: {self.Genero}, "
                f"Arma: {self.Arma}, Clase: {self.Clase}")

    def saludar(self):
        print(f"Hola {self.Nombre}, ¿cómo estás?")


# Lista de personajes
personajes = [
    Personaje('Arthur', 'Masculino', 'Hacha', 'Asesino'),
    Personaje('Seraphine', 'Femenino', 'Libro mágico', 'Daño mágico'),
    Personaje('Korvos', 'Masculino', 'Katana', 'Espadachín'),
    Personaje('Aelius', 'Femenino', 'Arco', 'Arquero'),
    Personaje('Valgrim', 'Femenino', 'Escudo y daga', 'Tanque'),
    Personaje('Aldren', 'Masculino', 'Katana', 'Espadachín')
]

# Imprimir y saludar a cada personaje
for personaje in personajes:
    print(personaje)
    personaje.saludar()
    print("---")
