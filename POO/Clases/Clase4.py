class Granja:
    def __init__(self, Animales, Hectareas, Produccion):
        self.Animales = Animales
        self.Hectareas = Hectareas
        self.Produccion = Produccion

Granja1 = Granja("30", "3", "100")

print(Granja1.Animales, Granja1.Hectareas, Granja1.Produccion)