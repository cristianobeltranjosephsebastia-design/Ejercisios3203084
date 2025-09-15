class Alumno:
    def __init__(self, Capacidad, Cuadernos, Curso, Boligrafo):
        self.Capacidad = Capacidad
        self.Cuadernos = Cuadernos
        self.Curso = Curso
        self.Boligrafo = Boligrafo

Estudiante1 = Alumno("8pax", "7", "1101", "Negro")

print(Estudiante1.Capacidad, Estudiante1.Cuadernos, Estudiante1.Curso, Estudiante1.Boligrafo)