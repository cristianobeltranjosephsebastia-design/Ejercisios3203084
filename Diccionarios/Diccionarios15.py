passwords = {'Admin': '1234', 'User': 'abcd', 'Guest': '0000'}
user = input("Enter a user: ")
print("Password:", passwords.get(user.title(), "No password found"))

