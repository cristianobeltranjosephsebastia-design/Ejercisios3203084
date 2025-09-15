planets = {'Earth': 3, 'Mars': 4, 'Jupiter': 5}
planet = input("Enter a planet: ")
print("Position from Sun:", planets.get(planet.title(), "Not found"))

