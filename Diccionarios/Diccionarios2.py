capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Italy': 'Rome'}
country = input("Enter a country: ")
print("Capital:", capitals.get(country.title(), "Not in dictionary"))

