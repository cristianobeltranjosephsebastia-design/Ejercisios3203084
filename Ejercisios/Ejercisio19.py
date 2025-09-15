Animals = ["perro", "gato", "pájaro", "pez", "hamster", "conejo", "gato"]
print("Lista de animales:", Animals)
Animal_search = "gato"
if Animal_search in Animals:
    print(f"\n7 {Animal_search} está en la lista")
    Position = Animals.index(Animal_search)
    print(f"Primera aparición en posición: {Position}")
    Amount = Animals.count(Animal_search)
    print(f"Aparece {Amount} veces en total")
else:
    print(f"\n{Animal_search} no está en la lista")
Search = ["gato", "serpiente", "pájaro"]
print(f"\nBuscando: {Search}")
for Animal in Search:
    if Animal in Animals:
        posicion = Animals.index(Animal)
        print(f"7 {Animal} encontrado en posición {Position}")
    else:
        print(f"{Animal} no encontrado")