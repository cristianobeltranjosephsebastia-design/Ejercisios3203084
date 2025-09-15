class Celulares:
    def __init__(self, Marca, Precio):
        self.Marca = Marca
        self.Precio = Precio

    def presentarse(self):
        return f"Hola, este es {self.Marca} y esta en {self.Precio} "


Celular = [
    Celulares("Oppo", "1.100.000"),
    Celulares("Samsung", "1.500.000"),
    Celulares("Apple", "2.200.000")
]


for Celulares in Celular:
    print(Celulares.presentarse())
