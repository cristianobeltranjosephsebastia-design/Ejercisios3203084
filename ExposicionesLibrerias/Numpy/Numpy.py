import numpy as np 


vector = np.array([1, 2, 3, 4, 5])
print("Vector:", vector)


suma = np.sum(vector)
media = np.mean(vector)
print("Suma del vector", suma)
print("Media del vector", media)



matriz = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Matriz original\n", matriz)

transpuesta = np.transpose(matriz)
print("Matriz transpuesta\n", transpuesta)


multiplicacion = np.dot(matriz, transpuesta)
print("Multiplicación \n", multiplicacion)