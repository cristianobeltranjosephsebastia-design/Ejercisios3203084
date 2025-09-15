def es_primo_simple(number):
    """
    Verifica si un número es primo usando método básico
    Un número primo solo es divisible por 1 y por sí mismo
    """
    if number < 2:
        return False

    print(f"Verificando si {number} es primo:")
    for i in range(2, int(number ** 0.5) + 1):  # Solo hasta la raíz cuadrada
        print(f" ¿{number} es divisible por {i}? ", end="")
        if number % i == 0:
            print(f"Sí ({number} / {i} = {number // i})")
            return False
        else:
            print("No")
    print(f" 7 {number} es primo")
    return True


def criba_eratostenes(limit):
    """
    Encuentra todos los primos hasta 'limit' usando la Criba de Eratóstenes
    Es más eficiente para encontrar múltiples primos
    """
    print(f"Aplicando Criba de Eratóstenes hasta {limit}")
    # Crear lista: True significa "posiblemente primo"
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 y 1 no son primos
    print(f"Lista inicial: {is_prime[:min(20, len(is_prime))]}...")
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            print(f"\nMarcando múltiplos de {i}:")
            # Marcar todos los múltiplos de i como no primos
            for j in range(i * i, limit + 1, i):
                if is_prime[j]:  # Solo mostrar si aún no estaba marcado
                    print(f" {j} (múltiplo de {i}) 3 No primo")
                    is_prime[j] = False
    # Recopilar números primos
    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


def factorizacion_prima(number):
    """
    Encuentra los factores primos de un número
    """
    print(f"\nFactorización prima de {number}:")
    factors = []
    divisor = 2
    temp_number = number
    while divisor * divisor <= temp_number:
        while temp_number % divisor == 0:
            factors.append(divisor)
            print(f" {temp_number} ÷ {divisor} = {temp_number // divisor}")
            temp_number //= divisor
        divisor += 1

    if temp_number > 1:
        factors.append(temp_number)
        print(f" Factor primo final: {temp_number}")
    return factors


# Probando generadores de primos
print("GENERADOR DE NÚMEROS PRIMOS")
print("=" * 40)

# Verificar si números individuales son primos
numbers_to_test = [17, 25, 29]
print("1. VERIFICACIÓN INDIVIDUAL:")
for num in numbers_to_test:
    result = es_primo_simple(num)
    print()

# Criba de Eratóstenes
print("\n2. CRIBA DE ERATÓSTENES:")
print("-" * 30)
primes_up_to_30 = criba_eratostenes(30)
print(f"\nPrimos encontrados hasta 30: {primes_up_to_30}")
print(f"Total de primos: {len(primes_up_to_30)}")

# Factorización prima
print("\n3. FACTORIZACIÓN PRIMA:")
print("-" * 30)
number_to_factorize = 60
factors = factorizacion_prima(number_to_factorize)
factors_str = " × ".join(map(str, factors))
print(f"\n{number_to_factorize} = {factors_str}")

# Verificación
product = 1
for factor in factors:
    product *= factor
print(f"Verificación: {factors_str} = {product}")
