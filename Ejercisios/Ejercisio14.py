Number = 1
Limit = 20
peers_found = 0

print("Buscando numeros pares entre 1 y", Number, "limite", Limit)

while Number <= Limit:
    if Number %2 == 0:
        print(Number, "Es par")
        peers_found = peers_found + 1
        Number = Number + 1

print("/n Resumen")
print("Se encontraron ", peers_found)