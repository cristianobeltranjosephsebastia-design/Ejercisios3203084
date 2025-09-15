weather = {'Sunny': 'Clear sky', 'Rainy': 'Umbrella needed', 'Snowy': 'Cold weather'}
condition = input("Enter weather condition: ")
print("Description:", weather.get(condition.title(), "Unknown condition"))
