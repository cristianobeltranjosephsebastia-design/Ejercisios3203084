def contar_frecuencias(lista):
    """
    Cuenta la frecuencia de cada elemento en la lista
    Retorna un diccionario con elemento: frecuencia
    """
    frequencies = {}  # Diccionario para almacenar resultados
    print(f"Analizando lista: {lista}")
    print("\nProceso de conteo:")
    for element in lista:
        if element in frequencies:
            frequencies[element] += 1
            print(f" {element}: incrementado a {frequencies[element]}")
        else:
            frequencies[element] = 1
            print(f" {element}: primer aparición")
    return frequencies

def encontrar_mas_frecuente(frequencies):
    """Encuentra el elemento que más se repite"""
    if not frequencies:
        return None, 0
    max_element = max(frequencies, key=frequencies.get)
    max_frequency = frequencies[max_element]
    return max_element, max_frequency

def mostrar_estadisticas(frequencies):
    """Muestra estadísticas detalladas"""
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DE FRECUENCIA")
    print("=" * 40)
    # Ordenar por frecuencia (mayor a menor)
    ordered_frequencies = sorted(frequencies.items(),
                                 key=lambda x: x[1],
                                 reverse=True)

    total_elements = sum(frequencies.values())
    unique_elements = len(frequencies)
    print(f"Total de elementos: {total_elements}")
    print(f"Elementos únicos: {unique_elements}")
    print("\nFrecuencias (ordenadas por cantidad):")
    for element, frequency in ordered_frequencies:
        percentage = (frequency / total_elements) * 100
        bar = "-" * frequency  # Gráfico de barras simple
        print(f" {element:>3}: {frequency:>2} veces ({percentage:4.1f}%) {bar}")
    # Elemento más frecuente
    most_frequent, max_freq = encontrar_mas_frecuente(frequencies)
    print(f"\nElemento más frecuente: {most_frequent} ({max_freq} veces)")

# Probando el contador de frecuencias
print("CONTADOR DE FRECUENCIAS")
print("=" * 30)

# Ejemplo con números
numbers = [1, 2, 3, 2, 1, 4, 2, 5, 2, 1, 3, 2]
frequencies_num = contar_frecuencias(numbers)
mostrar_estadisticas(frequencies_num)

# Ejemplo con letras
print("\n" + "=" * 50)
text = "programacion"
letters = list(text)  # Convierte el texto en lista de caracteres
print(f"\nAnalizando la palabra: '{text}'")
frequencies_letters = contar_frecuencias(letters)
mostrar_estadisticas(frequencies_letters)
