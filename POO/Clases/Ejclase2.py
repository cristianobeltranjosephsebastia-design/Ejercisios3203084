
class Productos: 
    def __init__(self, Precio, Producto):
        self.Precio = Precio
        self.Producto = Producto

    def __str__(self):
        return f"{'Producto'}, {'precio'}"
    
    def __repr__ (self):
        return f"{self.Precio}, {self.Producto}"


class Producto:
    def __format__(self, formato):
        if formato == "Precio":
            return f"{self.Precio}"
        return str(self)
    
Producto1 = Productos("3.000.000", "Computador")

print(Producto1)
print(repr(Producto1))
print(f"{Producto1.Precio}")
