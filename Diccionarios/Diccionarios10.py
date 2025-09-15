sports = {'Soccer': 11, 'Basketball': 5, 'Tennis': 2}
sport = input("Enter a sport: ")
print("Players:", sports.get(sport.title(), "Unknown sport"))

