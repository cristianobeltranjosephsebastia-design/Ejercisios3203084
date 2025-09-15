Note = float(input("Digite su nota final (del 1 al 100)"))

if Note >= 9.0:
    classification = "Excelente"
    Message = "Felicidades Eres de los mejores"
elif Note >= 7.0:
    classification = "Bueno"
    Message = "Buen trabajo puedes mejorar"
else:
    classification= "Necesitas mejorar"
    Message = "Haz tu mejor esfuerzo para la proxima"

print("Tu nota es:", Note)
print("Tu clasificacion es", classification)
print("Tu mensaje es:", Message)