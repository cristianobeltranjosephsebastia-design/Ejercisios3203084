def Addition(a, b):
    """Suma dos números y devuelve el resultado"""
    Result = a + b
    return Result

def Substraction(a, b):
    """Resta b de a y devuelve el resultado"""
    Result = a - b
    return Result

def Multiplication(a, b):
    """Multiplica dos números y devuelve el resultado"""
    Result = a * b
    return Result

def Split(a, b):
    """Divide a entre b y devuelve el resultado"""
    if b != 0:
        Result = a / b
        return Result
    else:
        return "Error: No se puede dividir entre cero"


num1 = 20
num2 = 10

print("CALCULADORA CON FUNCIONES")
print(f"Números a operar: {num1} y {num2}")
print("-" * 30)
print(f"{num1} + {num2} = {Addition(num1, num2)}")
print(f"{num1} - {num2} = {Substraction(num1, num2)}")
print(f"{num1} * {num2} = {Multiplication(num1, num2)}")
print(f"{num1} / {num2} = {Split(num1, num2)}")
print(f"{num1} / 0 = {Split(num1, 0)}")