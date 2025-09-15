Numbers = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]

print("Lista original:", Numbers)
print("Cantidad de elementos:", len(Numbers))
Numbers_upward = Numbers.copy()
Numbers_falling = Numbers.copy()
Numbers_falling.sort()
print("\nOrdenada ascendente:", Numbers_upward)
Numbers_falling.sort(reverse=True)
print("Ordenada descendente:", Numbers_falling)

import random
Numbers_mixed = Numbers.copy()
random.shuffle(Numbers_mixed)
print("Lista mezclada:", Numbers_mixed)
numeros_invested = Numbers.copy()
numeros_invested.reverse()
print("Orden invertido:", numeros_invested)
print("\nLista original (sin cambios):", Numbers)