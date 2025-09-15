ages = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
name = input("Enter a name: ")
print("Age:", ages.get(name.title(), "Not found"))

