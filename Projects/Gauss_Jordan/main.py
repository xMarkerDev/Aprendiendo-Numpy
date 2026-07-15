import numpy as np
from escalar import definir_Matriz_Escalar, resultado
from newMatriz import mostrar_menu, definir_dimension, crear_matriz, formatear_matriz_fracciones

  
filas, columnas = definir_dimension()
matriz_original = crear_matriz(filas, columnas)
matriz_actual = matriz_original.copy()
matriz_string = formatear_matriz_fracciones(matriz_actual)

print("Matriz inicial:")
print(matriz_actual)
print(matriz_string)
print(type(matriz_actual))

#lista = np.array([1, 2, 3, 4], dtype=object)
lista = np.array([1, 2, 3, 4])


matriz_Escalar = definir_Matriz_Escalar(matriz_actual)
resultado(matriz_Escalar)

# while True:
#     mostrar_menu()
#     opcion = input("Elige una opción (1-5): ").strip()

#     if opcion == "5":
#         print("¡Hasta luego!")
#         break

#     elif opcion == "4":
#         print("\nEstado actual de la matriz:")
#         print(matriz_actual)
        
#     elif opcion in ("1", "2", "3"):
      
#       if opcion == "1":
#         print("hoola")
        
#       elif opcion == "2":
#         print("hoola")
        
      