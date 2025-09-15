class Objetos:
    def __init__(self, Nombre, ):
        self.Nombre = Nombre
        self.elementos = []

    def agregar_elementos(self, elemento):
        self.elementos.append(elemento)

    def mostrar_elementos(self):
        print(f"Elemento agregado: {self.Nombre}, {self.elementos}")    

Objeto1 = Objetos ("Objetos")
Objeto1.agregar_elementos("Objeto1")
Objeto1.agregar_elementos("Objeto2")

Objeto1.mostrar_elementos()