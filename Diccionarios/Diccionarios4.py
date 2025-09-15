grades = {'Math': 90, 'English': 85, 'History': 78}
subject = input("Enter a subject: ")
print("Grade:", grades.get(subject.title(), "Not available"))

