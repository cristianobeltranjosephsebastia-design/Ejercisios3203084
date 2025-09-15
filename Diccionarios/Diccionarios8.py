cars = {'Toyota': 'Japan', 'BMW': 'Germany', 'Ford': 'USA'}
brand = input("Enter a car brand: ")
print("Origin:", cars.get(brand.title(), "Brand not listed"))

