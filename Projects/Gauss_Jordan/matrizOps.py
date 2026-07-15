# matriz_ops.py
# Creación, formateo y operaciones sobre matrices de fracciones

import numpy as np
from fractions import Fraction
from utils import sol_Escalar, sol_Numero_De_Fila

# ---------- Creación de la matriz ----------
def crear_matriz(n, m, max_num=10, max_den=10):
    """
    Genera una matriz de tamaño n x m con elementos Fraction aleatorios.
    Los numeradores y denominadores se generan entre 1 y max_num/max_den respectivamente.
    """
    rng = np.random.default_rng(seed=42)
    numeradores = rng.integers(low=1, high=max_num+1, size=(n, m))
    denominadores = rng.integers(low=1, high=max_den+1, size=(n, m))
    
    # Crear array de objetos vacío y llenarlo con Fraction
    matriz = np.empty((n, m), dtype=object)
    for i in range(n):
        for j in range(m):
            matriz[i, j] = Fraction(numeradores[i, j], denominadores[i, j])
    return matriz


def formatear_matriz_fracciones(matriz):
    """
    Convierte una matriz de Fraction en una cadena con formato legible.
    Los denominadores iguales a 1 se omiten (muestra solo el numerador).
    """
    def fmt(x):
        if isinstance(x, Fraction):
            return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
        return str(x)
    return np.array2string(matriz, formatter={'object': fmt})


def resultado(matriz):
    """Imprime la matriz con formato amigable."""
    print("Matriz:")
    print(formatear_matriz_fracciones(matriz))


def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nOperaciones para Gauss-Jordan")
    print("1. Cambiar filas")
    print("2. Multiplicar fila por escalar")
    print("3. Sumar filas")
    print("4. Mostrar matriz actual")
    print("5. Salir")


# ---------- Operaciones sobre filas ----------
def operacion_Es_Fil(esc, fil):
    """
    Multiplica una fila (array de Fraction) por un escalar (Fraction).
    Retorna un nuevo array con el resultado.
    """
    return esc * fil.astype(object)


def operacion_Sum_Fil(fil_1, fil_2):
    """
    Suma dos filas (arrays de Fraction) elemento a elemento.
    Retorna un nuevo array con la suma.
    """
    return fil_1.astype(object) + fil_2.astype(object)


def definir_Matriz_Escalar(matriz_Nueva):
    """
    Pide el número de fila y el escalar, multiplica esa fila por el escalar.
    Retorna una nueva matriz modificada (copia).
    """
    n_fila = sol_Numero_De_Fila(max_filas=matriz_Nueva.shape[0])
    n_escalar = sol_Escalar()
    
    matriz = np.copy(matriz_Nueva)  # Copia explícita
    matriz[n_fila-1] = operacion_Es_Fil(n_escalar, matriz[n_fila-1])
    return matriz


def definir_Matriz_Suma(Matriz_Nueva):
    """
    Pide dos números de fila y suma la segunda a la primera (R_i ← R_i + R_j).
    Retorna una nueva matriz modificada (copia).
    """
    n1 = sol_Numero_De_Fila("Número de fila destino (1): ", max_filas=Matriz_Nueva.shape[0])
    n2 = sol_Numero_De_Fila("Número de fila origen (2): ", max_filas=Matriz_Nueva.shape[0])
    
    matriz = np.copy(Matriz_Nueva)
    matriz[n1-1] = operacion_Sum_Fil(matriz[n1-1], matriz[n2-1])
    return matriz


def definir_Matriz_Intercambio(Matriz_Nueva):
    """
    Pide dos números de fila y las intercambia.
    Retorna una nueva matriz modificada (copia).
    """
    n1 = sol_Numero_De_Fila("Número de fila 1: ", max_filas=Matriz_Nueva.shape[0])
    n2 = sol_Numero_De_Fila("Número de fila 2: ", max_filas=Matriz_Nueva.shape[0])
    
    matriz = np.copy(Matriz_Nueva)
    # Intercambio directo usando indexación avanzada
    matriz[[n1-1, n2-1]] = matriz[[n2-1, n1-1]]
    return matriz
