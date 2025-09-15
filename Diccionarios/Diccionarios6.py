animals = {'Dog': 'Mammal', 'Eagle': 'Bird', 'Snake': 'Reptile'}
animal = input("Enter an animal: ")
print("Category:", animals.get(animal.title(), "Not recognized"))

