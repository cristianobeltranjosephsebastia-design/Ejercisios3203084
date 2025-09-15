import random
number = random.randint(1, 10)
guess = 0
while guess != number:
    guess = int(input("Guess the number: "))
print("Correct! The number was", number)

