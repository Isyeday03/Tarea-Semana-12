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