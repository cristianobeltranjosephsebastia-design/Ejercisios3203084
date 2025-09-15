computers = {'CPU': 'Processor', 'RAM': 'Memory', 'HDD': 'Storage'}
part = input("Enter a computer part: ")
print("Definition:", computers.get(part.upper(), "Not in dictionary"))

