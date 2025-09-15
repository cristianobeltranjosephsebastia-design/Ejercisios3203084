books = {'1984': 'George Orwell', 'Hamlet': 'Shakespeare', 'Odyssey': 'Homer'}
book = input("Enter a book: ")
print("Author:", books.get(book.title(), "Not listed"))
