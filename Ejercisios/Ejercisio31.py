def calcular_similitud(user1, user2):
    """
    Calcula similitud entre dos usuarios basada en gustos comunes
    Retorna un valor entre 0 (muy diferentes) y 1 (muy similares)
    """
    common_likes = 0
    total_comparisons = 0
    # Comparar cada categoría
    for category in user1:
        if category in user2:
            total_comparisons += 1
            # Si ambos tienen el mismo gusto (True/True o False/False)
            if user1[category] == user2[category]:
                common_likes += 1
    if total_comparisons == 0:
        return 0

    similarity = common_likes / total_comparisons
    return round(similarity, 2)


def encontrar_usuarios_similares(target_user, users_db, threshold=0.6):
    """
    Encuentra usuarios similares al usuario objetivo
    """
    similar_users = []
    print(f"Buscando usuarios similares a '{target_user}'")
    print(f"Umbral de similitud: {threshold}")
    print("-" * 40)
    target_likes = users_db[target_user]
    for user_name, user_likes in users_db.items():
        if user_name != target_user:
            similarity = calcular_similitud(target_likes, user_likes)
            print(f"{user_name}: similitud = {similarity}")
            if similarity >= threshold:
                similar_users.append((user_name, similarity))
    # Ordenar por similitud (mayor a menor)
    similar_users.sort(key=lambda x: x[1], reverse=True)
    return similar_users


def recomendar_contenido(target_user, similar_users, users_db):
    """
    Recomienda contenido basado en usuarios similares
    """
    target_likes = users_db[target_user]
    recommendations = {}
    print(f"\nGenerando recomendaciones para '{target_user}':")
    for similar_name, similarity in similar_users:
        similar_likes = users_db[similar_name]
        print(f"\nAnalizando gustos de {similar_name} (similitud: {similarity}):")
        for category, likes_it in similar_likes.items():
            # Si al usuario similar le gusta algo que el objetivo no ha probado
            if category not in target_likes and likes_it:
                if category not in recommendations:
                    recommendations[category] = []
                recommendations[category].append((similar_name, similarity))
                print(f" 3 Recomendar '{category}' (le gusta a {similar_name})")
    return recommendations


# Base de datos de usuarios y sus gustos
users = {
    "Ana": {
        "acción": True, "comedia": True, "drama": False,
        "terror": False, "ciencia_ficción": True
    },
    "Carlos": {
        "acción": True, "comedia": False, "drama": True,
        "terror": False, "ciencia_ficción": True
    },
    "María": {
        "acción": False, "comedia": True, "drama": True,
        "terror": True, "ciencia_ficción": False
    },
    "Pedro": {
        "acción": True, "comedia": True, "drama": False,
        "terror": False, "ciencia_ficción": False
    },
    "Laura": {
        "acción": False, "comedia": True, "drama": True,
        "terror": False, "ciencia_ficción": True
    }
}

print("SISTEMA DE RECOMENDACIONES")
print("=" * 35)

# Mostrar base de usuarios
print("Base de usuarios:")
for user, likes in users.items():
    print(f"{user}: {likes}")

print("\n" + "=" * 50)

# Buscar similares para Ana
target_user = "Ana"
similar_users = encontrar_usuarios_similares(target_user, users, 0.4)
print(f"\nUsuarios similares a {target_user}:")
for similar, similarity in similar_users:
    print(f" {similar}: {similarity * 100:.0f}% similar")

# Generar recomendaciones
recommendations = recomendar_contenido(target_user, similar_users, users)
print(f"\n" + "=" * 30)
print("RECOMENDACIONES FINALES")
print("=" * 30)
if recommendations:
    for category, recommenders in recommendations.items():
        print(f"\n")
