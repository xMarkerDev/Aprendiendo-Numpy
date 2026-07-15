from fractions import Fraction
import numpy as np

#Menu
def mostrar_menu():
    print("Operaciones para Gauss-Jordan")
    print("1. Cambiar filas")
    print("2. Multiplicar fila por escalar")
    print("3. Sumar filas")
    print("4. Mostrar matriz actual")
    print("5. Salir")
    
#Definir dimensiones de la matriz
def definir_dimension():
    while True:
        try:
            filas = int(input("Número de filas: "))
            columnas = int(input("Número de columnas: "))
            if filas <= 0 or columnas <= 0:
                print("Las dimensiones deben ser positivas.\n")
                continue
            return filas, columnas
        except ValueError:
            print("Error: introduce números enteros válidos.\n")

def crear_matriz(n, m, max_num=10, max_den=10):
    rng = np.random.default_rng(seed=42)
    
    # Generar numeradores y denominadores aleatorios
    numeradores = rng.integers(low=1, high=max_num+1, size=(n, m))
    denominadores = rng.integers(low=1, high=max_den+1, size=(n, m))
    
    # Crear array de Fraction combinando numeradores y denominadores
    matriz = np.empty((n, m), dtype=object)
    for i in range(n):
        for j in range(m):
            matriz[i, j] = Fraction(numeradores[i, j], denominadores[i, j])
    return matriz
  
def formatear_matriz_fracciones(matriz):
    def fmt(x):
        if isinstance(x, Fraction):
            # Si denominador es 1, solo muestra el numerador
            # if x.denominator == 1:
            #     return str(x.numerator)
            return f"{x.numerator}/{x.denominator}"
        return str(x)
    
    return np.array2string(matriz, formatter={'object': fmt})
