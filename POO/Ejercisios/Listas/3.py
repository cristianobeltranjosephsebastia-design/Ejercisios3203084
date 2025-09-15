class Vehiculos:
    def __init__(self, Marca):
        self.Marca = Marca
        self.elementos = [] 

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento) 

    def mostrar_elementos(self):
        print(f"Modelos en {self.Marca}: {self.elementos}")


Auto1 = Vehiculos("Audi")
Auto1.agregar_elemento("Sedan")
Auto1.agregar_elemento("R8")
Auto1.mostrar_elementos()

