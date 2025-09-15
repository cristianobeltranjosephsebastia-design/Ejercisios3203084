class Motos:
    def __init__(self, Modelo, Precio):
        self.Modelo = Modelo
        self.Precio = Precio

    def __repr__(self):
        return f"El modelo es'{self.Modelo}', y su precio es {self.Precio})"


Moto1 = Motos("RTR Apache", "15.000.000")

print(Moto1)
print(repr(Moto1))

