attempts = 0
pin = ""
while pin != "1234" and attempts < 3:
    pin = input("Enter PIN: ")
    attempts += 1
if pin == "1234":
    print("Correct PIN")
else:
    print("Card blocked")

