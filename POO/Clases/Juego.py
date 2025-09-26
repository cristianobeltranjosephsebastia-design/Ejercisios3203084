import random

class Personaje:
    def __init__(self, Nombre, Genero, Arma, Clase):
        self.Nombre = Nombre
        self.Genero = Genero
        self.Arma = Arma
        self.Clase = Clase
        self.vida = 100  

    def __str__(self):
        return f"Nombre: {self.Nombre} | Género: {self.Genero} | Arma: {self.Arma} | Clase: {self.Clase} | Vida: {self.vida}"

    def saludar(self):
        print(f"Hola, soy {self.Nombre}, un {self.Clase} con {self.Arma}.")

    def atacar(self, enemigo):
        
        base = random.randint(10, 20)
        if "Katana" in self.Arma:
            base += 5
        elif "Libro mágico" in self.Arma:
            base += 8
        elif "Hacha" in self.Arma:
            base += 12
        elif "Arco" in self.Arma:
            base += 6
        elif "Escudo" in self.Arma:
            base += 3  

        enemigo.vida -= base
        print(f"{self.Nombre} ataca con {self.Arma} a {enemigo.Nombre} y causa {base} de daño!")
        if enemigo.vida <= 0:
            print(f"☠️ {enemigo.Nombre} ha caído en batalla.")



personajes = [
    Personaje('Arthur', 'Masculino', 'Hacha', 'Asesino'),
    Personaje('Seraphine', 'Femenino', 'Libro mágico', 'Daño mágico'),
    Personaje('Korvos', 'Masculino', 'Katana', 'Espadachín'),
    Personaje('Aelius', 'Femenino', 'Arco', 'Arquero'),
    Personaje('Valgrim', 'Femenino', 'Escudo y daga', 'Tanque'),
    Personaje('Aldren', 'Masculino', 'Katana', 'Espadachín')
]


print("🎮 Bienvenido al Juego de Combate Épico 🎮\n")
print("Elige tu personaje:\n")

for i, p in enumerate(personajes, start=1):
    print(f"{i}. {p.Nombre} ({p.Clase} con {p.Arma})")


opcion = int(input("\n👉 Ingresa el número de tu personaje: ")) - 1
jugador = personajes[opcion]
print(f"\nHas elegido a {jugador.Nombre} ⚔️")


enemigos = personajes[:opcion] + personajes[opcion+1:]
enemigo = random.choice(enemigos)
print(f"Tu rival es {enemigo.Nombre} ({enemigo.Clase} con {enemigo.Arma})\n")


turno = 0
while jugador.vida > 0 and enemigo.vida > 0:
    if turno % 2 == 0:
        jugador.atacar(enemigo)
    else:
        enemigo.atacar(jugador)

    print(f"💙 Vida {jugador.Nombre}: {jugador.vida} | ❤️ Vida {enemigo.Nombre}: {enemigo.vida}\n")
    turno += 1

if jugador.vida > 0:
    print(f"🎉 {jugador.Nombre} ha ganado la batalla!")
else:
    print(f"💀 {enemigo.Nombre} te ha derrotado...")
