countries = {'Colombia': 'Bogota', 'Mexico': 'Mexico City', 'Canada': 'Ottawa'}
country = input("Enter a country: ")
print("Capital:", countries.get(country.title(), "Not found"))

