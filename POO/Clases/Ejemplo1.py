class persona:
    def __init__(self, Nombre, Apellido, Edad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad

persona1 = persona('Sebastian', 'Cristiano', '18')
persona2 = persona('Ivan', 'Malaver', '47')
persona3 = persona('Nicolas', 'Cristiano', '18')
persona4 = persona('David', 'Beltran', '17')
persona5 = persona('Fabian', 'Torres', '18')



persona1.Nombre = "Jesus"
persona5.Edad = '17'

print(persona1.Nombre)
print(persona2.Apellido)
print(persona3.Nombre)
print(persona4.Apellido)
print(persona5.Edad)