num_secreto = 11
Riddle = int(input("Elige un numero del 1 al 20"))

print("El numero secreto era:", num_secreto)
print("El numero que elegiste es:", Riddle)

if Riddle == num_secreto:
    print("FELICIDADES, Acertaste el numero")
elif Riddle < num_secreto:
    print("Tu numero es menor intenta con otro")
else:
    print("Tu numero es mayor intenta con otro")