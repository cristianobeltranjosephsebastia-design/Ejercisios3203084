class Estudiante:
    def __init__(self, nombre, clase):
        self.nombre = nombre
        self.clase = clase


estudiante1 = Estudiante("Ana", "Programacion")
estudiante2 = Estudiante("Luis", "Cocina")

print(estudiante1.nombre)
print(estudiante2.clase)

