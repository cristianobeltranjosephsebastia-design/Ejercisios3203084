class persona:
    def __init__(self, Peso, Cultura, Altura, Genero):
        self.Peso = Peso
        self.Cultura = Cultura
        self.Altura = Altura
        self.Genero = Genero

Sebastian = persona ("50 KG","Afro", "1.68cm", "Masculino")

print(Sebastian.Peso, Sebastian.Cultura, Sebastian.Altura, Sebastian.Genero)