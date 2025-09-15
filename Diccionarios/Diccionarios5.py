phones = {'Anna': '1234', 'Mark': '5678', 'Paul': '9012'}
person = input("Enter a person: ")
print("Phone:", phones.get(person.title(), "No number saved"))

