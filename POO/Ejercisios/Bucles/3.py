class Computador:
    def __init__(self, Marca, Precio):
        self.Marca = Marca
        self.Precio = Precio

    def presentarse(self):
        return f"Hola, este es el {self.Marca} y tiene un precio de {self.Precio} "


Computadores = [
    Computador("Asus", "3.200.000"),
    Computador("Lenovo", "2.000.000"),
    Computador("HP", "1.250.000")
]


for Computador in Computadores:
    print(Computador.presentarse())
