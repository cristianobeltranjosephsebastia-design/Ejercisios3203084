colors = {'Red': '#FF0000', 'Green': '#00FF00', 'Blue': '#0000FF'}
color = input("Enter a color: ")
print("Hex code:", colors.get(color.title(), "Unknown color"))

