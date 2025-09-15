Sum_total = 0
Num_actual = 1
Limit = 50

print("Sumando numeros del 1 al", Limit)

while Num_actual <= Limit:
    Sum_total = Sum_total + Num_actual 
    print("Sumando", Num_actual, "Total hasta hora", Sum_total)
    Num_actual = Num_actual + 1

print("/n Resultado Final")
print("La suma de todos los numeros del 1 al", Limit, "Es", Sum_total) 