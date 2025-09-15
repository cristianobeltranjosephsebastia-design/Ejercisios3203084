class Computador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"

class Orden:
    def __init__(self, id_orden, *computadores):
        self.id_orden = id_orden
        self.lista_computadores = list(computadores) 

    def __str__(self):
        computadores_str = "\n".join(str(c) for c in self.lista_computadores)
        return f"Orden #{self.id_orden}:\n{computadores_str}"

compu1 = Computador("Dell", "XPS")
compu2 = Computador("Apple", "MacBook")


orden1 = Orden(101, compu1, compu2)
print(orden1)
