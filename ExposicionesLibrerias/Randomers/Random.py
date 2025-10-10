import random

print(random.random())
print(random.randint(1, 10))
colores = ["rojo", "verde", "azul", "amarillo"]
print(random.choice(colores))
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)