languages = {'Python': 'Easy', 'C++': 'Hard', 'Java': 'Medium'}
lang = input("Enter a programming language: ")
print("Difficulty:", languages.get(lang.title(), "Not in list"))

