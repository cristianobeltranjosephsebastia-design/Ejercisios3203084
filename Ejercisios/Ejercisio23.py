def Word_count(Text):
    """Cuenta cuántas palabras hay en un texto"""
    Words = Text.split()
    return len(Words)
def Characters_count(Text, Include_space=True):
    """Cuenta los caracteres del texto"""
    if Include_space:
        return len(Text)
    else:
        return len(Text.replace(" ", ""))
def Find_longest_word(Text):
    """Encuentra la palabra más larga en el texto"""
    Words = Text.split()
    Longest_word = ""
    for Words in Words:
        if len(Words) > len(Longest_word):
            Longest_word = Words
    return Longest_word
def es_palindromo(Text):
    """Verifica si un texto es palíndromo (se lee igual al revés)"""
    Clean_text = Text.lower().replace(" ", "")
    Inverted_text = Clean_text[::-1]
    return Clean_text == Inverted_text

Phrase = "La programación es divertida y educativa"
print("ANALIZADOR DE TEXTO")
print(f"Texto: '{Phrase}'")
print("-" * 50)
print(f"Palabras: {Word_count(Phrase)}")
print(f"Caracteres (con espacios): {Characters_count(Phrase)}")
print(f"Caracteres (sin espacios): {Characters_count(Phrase, False)}")
print(f"Palabra más larga: '{Find_longest_word(Phrase)}'")
print(f"¿Es palíndromo?: {es_palindromo(Phrase)}")

palindromo = "anita lava la tina"
print(f"\nProbando palíndromo: '{palindromo}'")
print(f"¿Es palíndromo?: {es_palindromo(palindromo)}")