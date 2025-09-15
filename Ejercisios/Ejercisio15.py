Number_secret = 7
Tried_max = 3
Tried_current = 1

print("¡Bienvenido al juego de adivinanza!")
print("Tienes", Tried_max, "intentos para adivinar el número del 1 al 10")

while Tried_current <= Tried_max:
    print("\n--- Intento", Tried_current, "de", Tried_max, "---") 

    if Tried_current == 1:
        Riddle = 3
    elif Tried_current == 2:
        Riddle = 8
    else:
        Riddle = 7
    print("Tu adivinanza:", Riddle)
    if Riddle == Number_secret:
        print("¡GANASTE! El número era", Number_secret)
        break
    elif Riddle < Number_secret:
        print("El número es mayor")
    else:
        print("El número es menor")
    Tried_current = Tried_current + 1
    if Tried_current > Tried_max:
        print("\n¡Se acabaron los intentos! El número era", Number_secret)