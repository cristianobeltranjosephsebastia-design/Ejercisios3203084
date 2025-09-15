food = {'Apple': 52, 'Banana': 89, 'Orange': 47}
fruit = input("Enter a fruit: ")
print("Calories:", food.get(fruit.title(), "Not available"))

