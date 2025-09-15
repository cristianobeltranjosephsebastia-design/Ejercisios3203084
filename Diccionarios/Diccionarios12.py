months = {'January': 31, 'February': 28, 'March': 31}
month = input("Enter a month: ")
print("Days:", months.get(month.title(), "Not in dictionary"))

