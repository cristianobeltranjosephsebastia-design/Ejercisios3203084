currencies = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
currency = input("Enter a currency: ")
print(currencies.get(currency.title(), "Currency not found."))

