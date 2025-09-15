Number = int(input("Ingrese el numero de la tabla de multiplicar que requiera"))
Multiplier = 1

print("Tabla de multiplicar del", Number, ":")
print("=" * 25)

while Multiplier <= 10:
    Result = Number * Multiplier
    print(Number, "*",  Multiplier, "=", Result)
    Multiplier = Multiplier + 1
print("=" * 25)
print("Tabla completa")