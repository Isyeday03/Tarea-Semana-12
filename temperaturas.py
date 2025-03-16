import random

# Definir dimensiones de la matriz
ciudades = ["Loja", "Zamora", "Machala"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Crear la matriz 3D con temperaturas aleatorias entre 15 y 35 grados
temperaturas = {
    ciudad: [[random.randint(15, 31) for _ in dias_semana] for _ in range(num_semanas)]
    for ciudad in ciudades
}

def calcular_promedio_temperaturas(datos):
    for ciudad, semanas in datos.items():
        print(f"\nPromedio de temperaturas para {ciudad}:")
        promedios = []
        for i, semana in enumerate(semanas, start=1):
            promedio = sum(semana) / len(semana)
            promedios.append(promedio)
            print(f"  Semana {i}: {promedio:.2f}°C")
       
        semana_max = promedios.index(max(promedios)) + 1
        semana_min = promedios.index(min(promedios)) + 1
        print(f"  Semana con la temperatura más alta: Semana {semana_max} con {max(promedios):.2f}°C")
        print(f"  Semana con la temperatura más baja: Semana {semana_min} con {min(promedios):.2f}°C")

# Ejecutar la función
calcular_promedio_temperaturas(temperaturas)

# Nueva función: Calcula la temperatura promedio de cada ciudad durante todo el período
def calcular_temperatura_promedio_ciudad(datos_temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante todo el período de tiempo.
    
    Args:
        datos_temperaturas (dict): Un diccionario donde las claves son nombres de ciudades y 
                                  los valores son listas de listas con temperaturas diarias por semana.
    
    Returns:
        dict: Un diccionario con las ciudades como claves y sus temperaturas promedio como valores.
    """
    promedios_ciudades = {}
    
    for ciudad, semanas in datos_temperaturas.items():
        # Aplanar la lista de listas para obtener todas las temperaturas de la ciudad
        todas_temperaturas = []
        for semana in semanas:
            todas_temperaturas.extend(semana)
        
        # Calcular el promedio de todas las temperaturas de la ciudad
        promedio = sum(todas_temperaturas) / len(todas_temperaturas)
        promedios_ciudades[ciudad] = round(promedio, 2)
    
    return promedios_ciudades

# Prueba de la nueva función
def mostrar_temperaturas_promedio():
    print("\n--- TEMPERATURAS PROMEDIO POR CIUDAD ---")
    promedios = calcular_temperatura_promedio_ciudad(temperaturas)
    
    for ciudad, promedio in promedios.items():
        print(f"{ciudad}: {promedio}°C")
    
    # Encontrar la ciudad más caliente y la más fría
    ciudad_mas_caliente = max(promedios, key=promedios.get)
    ciudad_mas_fria = min(promedios, key=promedios.get)
    
    print(f"\nCiudad más caliente: {ciudad_mas_caliente} con {promedios[ciudad_mas_caliente]}°C")
    print(f"Ciudad más fría: {ciudad_mas_fria} con {promedios[ciudad_mas_fria]}°C")

# Ejecutar las funciones
if __name__ == "__main__":
    # Mostrar los promedios por semana (función original)
    calcular_promedio_temperaturas(temperaturas)
    
    # Mostrar los promedios por ciudad (nueva función)
    mostrar_temperaturas_promedio()