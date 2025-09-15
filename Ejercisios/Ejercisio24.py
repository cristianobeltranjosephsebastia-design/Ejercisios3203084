import random
import string
def Generate_password(Lenght=8, Include_capital_letter=True, Include_Numbers=True, Include_Symbols=False):
    """Genera una contraseña aleatoria con las características especificadas"""
    Characters = string.ascii_lowercase
    if Include_capital_letter:
        Characters += string.ascii_uppercase
    if Include_Numbers:
        Characters += string.digits
    if Include_Symbols:
        Characters += "!@#$%&*"

    Password = ""
    for i in range(Lenght):
        Random_characters = random.choice(Characters)
        Password += Random_characters
    return Password

def Evaluate_strength(Password):
    """Evalúa qué tan fuerte es una contraseña"""
    Points = 0
    Comments = []

    if len(Password) >= 8:
        Points += 2
        Comments.append("7 Longitud adecuada")
    else:
        Comments.append("' Muy corta (mínimo 8 caracteres)")

    if any(c.isupper() for c in Password):
        Points += 1
        Comments.append("7 Contiene mayúsculas")
    else:
        Comments.append("' Sin mayúsculas")
    if any(c.isdigit() for c in Password):
        Points += 1
        Comments.append("7 Contiene números")
    else:
        Comments.append("' Sin números")
    if Points >= 4:
        Strength = "Muy fuerte"
    elif Points >= 3:
        Strength = "Fuerte"
    elif Points >= 2:
        Strength = "Moderada"
    else:
        Strength = "Débil"

    return Strength, Comments


print("GENERADOR DE CONTRASEÑAS")
print("=" * 40)
Password1 = Generate_password(12, True, True, False)
Password2 = Generate_password(8, True, True, True)
Password3 = Generate_password(6, False, False, False)
Passwords = [
("Estándar (12 caracteres)", Password1),
("Con símbolos (8 caracteres)", Password2),
("Solo minúsculas (6 caracteres)", Password3)
]
for Description, Password in Passwords:
    Strength, Comments = Evaluate_strength(Password)
    print(f"\n{Description}:")
    print(f"Contraseña: {Password}")
    print(f"Fortaleza: {Strength}")
for Comment in Comments:
    print(f" {Comment}")