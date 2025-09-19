class Personaje:
    def __init__(self, Nombre, Genero, Arma, Clase):
        self.Nombre = Nombre
        self.Genero = Genero
        self.Arma = Arma
        self.Clase = Clase

    def __str__(self):
        return f"Nombre del personaje: {self.Nombre} y su genero es: {self.Genero} Tiene de arma: {self.Arma} y su clase es: { self.Clase}"
    
    def saludar(self):
        print( f"Hola {self.Nombre} Como estas?")
    


personajes = [
    Personaje('Arthur', 'Masculino', 'Hacha', 'Asesino'),
    Personaje('Seraphine', 'Femenino', 'Libro mágico', 'Daño mágico'),
    Personaje('Korvos', 'Masculino', 'Katana', 'Espadachín'),
    Personaje('Aelius', 'Femenino', 'Arco', 'Arquero'),
    Personaje('Valgrim', 'Femenino', 'Escudo y daga', 'Tanque'),
    Personaje('Aldren', 'Masculino', 'Katana', 'Espadachín')
]


for personaje in personajes:
    print(personaje)
    personaje.saludar()
    print("---")
