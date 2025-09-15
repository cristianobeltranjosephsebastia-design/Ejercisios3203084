def saludar(Name):
    """Esta función saluda a una persona por su nombre"""
    Message = f"¡Hola {Name}! ¿Cómo estás?" 
    return Message 


Salute1 = saludar("Luis")
Salute2 = saludar("Sebastian")
Salute3 = saludar("María")

print("Usando mi función de saludo:")

print(Salute1)
print(Salute2)
print(Salute3)

print("\nUsando directamente:")
print(saludar("Pedro"))
print(saludar("Laura"))