import numpy as np
from escalar import definir_Matriz_Escalar, definir_Matriz_Suma, definir_Matriz_Intercambio
from newMatriz import resultado, definir_dimension, crear_matriz, mostrar_menu

filas, columnas = definir_dimension()
matriz_original = crear_matriz(filas, columnas)
matriz_actual = matriz_original.copy()

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ").strip()

    if opcion == "5":
        print("¡Hasta luego!")
        break

    elif opcion == "4":
        resultado(matriz_actual)
        
    elif opcion in ("1", "2", "3"):
      
      if opcion == "1":
        matriz_actual = definir_Matriz_Intercambio(matriz_actual)
        resultado(matriz_actual)
        
      elif opcion == "2":
        matriz_actual = definir_Matriz_Escalar(matriz_actual)
        resultado(matriz_actual)
        
      elif opcion == "3":
        matriz_actual = definir_Matriz_Suma(matriz_actual)
        resultado(matriz_actual)
        
      