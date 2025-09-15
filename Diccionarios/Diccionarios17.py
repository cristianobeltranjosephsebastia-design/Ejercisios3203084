music = {'Rock': 'Guitar', 'Jazz': 'Saxophone', 'Classical': 'Violin'}
genre = input("Enter a music genre: ")
print("Main instrument:", music.get(genre.title(), "Unknown genre"))

