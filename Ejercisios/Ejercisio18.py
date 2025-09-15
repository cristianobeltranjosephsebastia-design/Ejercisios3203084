Ratings = [8.5, 9.2, 7.8, 9.5, 6.9, 8.8, 9.1, 7.5]
print("Calificaciones del estudiante:")
print(Ratings)
total_matters = len(Ratings)
suma_notes = sum(Ratings)
prom = suma_notes / total_matters
note_mayor = max(Ratings)
note_menor = min(Ratings)
print(f"\n--- ESTADÍSTICAS ---")
print(f"Total de materias: {total_matters}")
print(f"Suma de todas las notas: {suma_notes}")
print(f"Promedio: {prom:.2f}")
print(f"Nota más alta: {note_mayor}")
print(f"Nota más baja: {note_menor}")
Approved = 0
for nota in Ratings:
    if nota >= 7.0:
        Approved = Approved + 1
        print(f"Materias aprobadas: {Approved} de {total_matters}")