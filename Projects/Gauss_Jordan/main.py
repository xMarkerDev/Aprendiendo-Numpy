# main.py
# Punto de entrada principal del programa

import numpy as np
from matrizOps import (
    crear_matriz, resultado, mostrar_menu,
    definir_Matriz_Escalar, definir_Matriz_Suma, definir_Matriz_Intercambio
)

def definir_dimension():
    """
    Solicita al usuario el número de filas y columnas para la matriz.
    Valida que sean enteros positivos.
    """
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

# ---------- Programa principal ----------
if __name__ == "__main__":
    print("Bienvenido al programa de operaciones con matrices de fracciones.")
    filas, columnas = definir_dimension()
    matriz_original = crear_matriz(filas, columnas)
    matriz_actual = np.copy(matriz_original)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break
        elif opcion == "4":
            resultado(matriz_actual)
        elif opcion == "1":
            matriz_actual = definir_Matriz_Intercambio(matriz_actual)
            resultado(matriz_actual)
        elif opcion == "2":
            matriz_actual = definir_Matriz_Escalar(matriz_actual)
            resultado(matriz_actual)
        elif opcion == "3":
            matriz_actual = definir_Matriz_Suma(matriz_actual)
            resultado(matriz_actual)
        else:
            print("Opción no válida. Intenta de nuevo.")