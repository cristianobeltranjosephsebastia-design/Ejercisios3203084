Total = int(input("Indique su precio total"))
Discount = 0

if Total > 2000:
    Discount = Total * 0.20
    P_fin = Total - Discount
    print("¡Eres afortunado!, Tienes un descuento del ¡20%!")
    print("Descuento aplicado", Discount)
else:
    P_fin = Total
    print("No hay un descuento disponible")

print("Precio original", Total, "y el precio final es", P_fin)