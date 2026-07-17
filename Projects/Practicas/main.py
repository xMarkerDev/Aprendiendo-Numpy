#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARCHIVO DE APRENDIZAJE PROFESIONAL DE NumPy
Incluye desde los fundamentos hasta operaciones avanzadas,
con explicaciones detalladas de cada atributo, función y técnica.
"""

import numpy as np

# -------------------------------------------------------------------
# 1. VERSIÓN DE NUMPY
# Siempre es buena práctica conocer la versión con la que trabajamos,
# ya que algunas funciones pueden variar entre versiones.
# -------------------------------------------------------------------
print("Versión de NumPy:", np.__version__)

# -------------------------------------------------------------------
# 2. DIFERENCIA FUNDAMENTAL ENTRE LISTAS Y ARRAYS
# Las listas de Python son contenedores heterogéneos; las operaciones
# aritméticas * replican la lista.
# Los arrays de NumPy son homogéneos y las operaciones se aplican
# elemento a elemento (vectorización).
# -------------------------------------------------------------------
lista = [1, 2, 3, 4]
lista = lista * 2          # [1,2,3,4,1,2,3,4]  -> concatena la lista consigo misma
print("Lista * 2:", lista)

array = np.array([1, 2, 3, 4])
array = array * 2          # [2,4,6,8]  -> cada elemento se multiplica por 2
print("Array * 2:", array)

# -------------------------------------------------------------------
# 3. CREACIÓN DE ARRAYS CON DIFERENTES DIMENSIONES
# Vamos a crear arrays de 0, 1, 2 y 3 dimensiones para entender
# los atributos fundamentales: ndim, shape, size y dtype.
# -------------------------------------------------------------------

# --- 3.0 Array de dimensión 0 (escalar) ---
escalar = np.array('A')
# ndim: número de dimensiones (0)
# shape: tupla con la longitud en cada eje (vacía para 0-D)
# size: número total de elementos (1)
# dtype: tipo de dato de los elementos (<U1 es cadena Unicode de longitud 1)
print("\n--- Escalar (0-D) ---")
print("Valor:", escalar)
print("ndim:", escalar.ndim)      # 0 -> sin ejes
print("shape:", escalar.shape)    # () -> tupla vacía
print("size:", escalar.size)      # 1
print("dtype:", escalar.dtype)    # <U1

# --- 3.1 Array de dimensión 1 (vector) ---
vector = np.array(['A', 'B', 'C'])
print("\n--- Vector (1-D) ---")
print("Valor:", vector)
print("ndim:", vector.ndim)       # 1 -> un eje
print("shape:", vector.shape)     # (3,) -> 3 elementos a lo largo del único eje
print("size:", vector.size)       # 3
print("dtype:", vector.dtype)     # <U1

# --- 3.2 Array de dimensión 2 (matriz) ---
matriz = np.array([['A', 'B', 'C'],
                   ['D', 'F', 'E'],
                   ['G', 'H', 'J']])
print("\n--- Matriz (2-D) ---")
print("Valor:\n", matriz)
print("ndim:", matriz.ndim)       # 2 -> filas y columnas
print("shape:", matriz.shape)     # (3,3) -> 3 filas, 3 columnas
print("size:", matriz.size)       # 9
print("dtype:", matriz.dtype)     # <U1

# --- 3.3 Array de dimensión 3 (tensor) ---
tensor_letras = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                          [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                          [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])
print("\n--- Tensor (3-D) ---")
print("Valor:\n", tensor_letras)
print("ndim:", tensor_letras.ndim)   # 3 -> ejes: profundidad, fila, columna
print("shape:", tensor_letras.shape) # (3,3,3) -> 3 bloques, 3 filas, 3 columnas
print("size:", tensor_letras.size)   # 27
print("dtype:", tensor_letras.dtype) # <U1

# -------------------------------------------------------------------
# 4. INDEXACIÓN EN ARRAYS MULTIDIMENSIONALES
# Se accede con la notación [eje0, eje1, eje2, ...]
# En un tensor 3D el orden suele ser (profundidad, fila, columna).
# Vamos a formar la palabra "HOLA" extrayendo caracteres.
# -------------------------------------------------------------------
# Cada elemento es una cadena de un carácter (dtype <U1),
# por lo que podemos sumarlos con + (concatenación de cadenas).
letra_H = tensor_letras[0, 2, 1]   # Bloque 0, fila 2, columna 1 -> 'H'
letra_O = tensor_letras[1, 1, 2]   # Bloque 1, fila 1, columna 2 -> 'O'
letra_L = tensor_letras[1, 0, 2]   # Bloque 1, fila 0, columna 2 -> 'L'
letra_A = tensor_letras[0, 0, 0]   # Bloque 0, fila 0, columna 0 -> 'A'

saludo = letra_H + letra_O + letra_L + letra_A
print("\nSaludo formado por indexación:", saludo)

# -------------------------------------------------------------------
# 5. SLICING (REBANADO) Y LA DIFERENCIA ENTRE VISTA Y COPIA
# El slicing devuelve una VISTA (mismo bloque de memoria), no una copia.
# Si modificas la vista, el array original cambia.
# Para copia independiente se usa .copy()
# -------------------------------------------------------------------
print("\n--- Slicing y vistas ---")
original = np.array([10, 20, 30, 40, 50])
vista = original[1:4]          # [20,30,40] – mismo lugar en memoria
copia_independiente = original[1:4].copy()

vista[0] = 999
print("Original tras modificar vista:", original)  # [10,999,30,40,50]
print("Copia independiente:", copia_independiente) # [20,30,40] no cambió

# Slicing en 2D
print("\nSlicing en matriz:")
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matriz original:\n", mat)
print("Fila 0 completa (mat[0, :]):", mat[0, :])      # [1 2 3]
print("Columna 1 completa (mat[:, 1]):", mat[:, 1])    # [2 5 8]
print("Submatriz 0:2, 1:3:\n", mat[0:2, 1:3])         # [[2,3],[5,6]]

# -------------------------------------------------------------------
# 6. CONTROL EXPLÍCITO DEL TIPO DE DATO (dtype)
# Puedes forzar el tipo al crear el array. Así ahorras memoria y ganas velocidad.
# -------------------------------------------------------------------
a_float = np.array([1, 2, 3], dtype=np.float32)   # 32 bits
a_int64 = np.array([1.5, 2.7], dtype=np.int64)    # trunca a entero
print("\nArray float32:", a_float, a_float.dtype)
print("Array int64 (truncado):", a_int64, a_int64.dtype)

# -------------------------------------------------------------------
# 7. FUNCIONES DE CREACIÓN DE ARRAYS MÁS COMUNES
# -------------------------------------------------------------------
ceros = np.zeros((3, 4))                       # matriz 3x4 de ceros (float por defecto)
unos = np.ones((2, 3, 2))                      # tensor de unos
identidad = np.eye(4)                          # matriz identidad 4x4
rango = np.arange(0, 10, 2)                    # [0,2,4,6,8]
puntos = np.linspace(0, 1, 5)                 # 5 valores equiespaciados entre 0 y 1

print("\nzeros:\n", ceros)
print("ones (shape 2,3,2):\n", unos)
print("eye(4):\n", identidad)
print("arange(0,10,2):", rango)
print("linspace(0,1,5):", puntos)

# -------------------------------------------------------------------
# 8. BROADCASTING
# Permite operar arrays de diferentes formas siguiendo reglas fijas.
# Los arrays se "estiran" virtualmente para coincidir en dimensiones.
# -------------------------------------------------------------------
a = np.array([1, 2, 3])          # shape (3,)
b = np.array([[10], [20]])       # shape (2,1)
c = a + b                        # (2,1) + (3,) -> broadcast a (2,3)
print("\nBroadcasting a + b:\n", c)
# Resultado:
# [[11, 12, 13],
#  [21, 22, 23]]

# -------------------------------------------------------------------
# 9. AGREGACIONES Y EL PARÁMETRO axis
# 'axis' indica sobre qué eje se colapsa la operación.
# axis=0 -> operación entre filas (reduce filas)
# axis=1 -> operación entre columnas (reduce columnas)
# -------------------------------------------------------------------
# Ejemplo: temperaturas diarias de 3 ciudades durante 7 días
temp = np.array([[15, 16, 14, 13, 18, 20, 22],   # Ciudad A
                 [10, 11, 12, 10,  9, 15, 17],   # Ciudad B
                 [20, 22, 23, 25, 24, 26, 27]])  # Ciudad C

print("\nTemperaturas (ciudades x días):\n", temp)

# Media por ciudad (colapsamos el eje de los días -> axis=1)
media_ciudad = temp.mean(axis=1)
print("Media de temperatura por ciudad:", media_ciudad)  # [16.857..., 12.571..., 23.857...]

# Temperatura media por día (colapsamos el eje de las ciudades -> axis=0)
temp_media_dia = temp.mean(axis=0)
print("Temperatura media por día:", temp_media_dia)

# Día más caluroso en promedio
dia_mas_caluroso = temp_media_dia.argmax()   # índice del valor máximo
print(f"Día más caluroso: día {dia_mas_caluroso+1} ({temp_media_dia[dia_mas_caluroso]:.1f}°C)")

# -------------------------------------------------------------------
# 10. MÁSCARAS BOOLEANAS (INDEXACIÓN LÓGICA)
# Podemos filtrar elementos usando condiciones.
# -------------------------------------------------------------------
ciudad_A = temp[0]   # primera fila
dias_calientes = ciudad_A > 16
print("\n¿Días en Ciudad A con temp > 16?:", dias_calientes)   # [False, False, False, False, True, True, True]
print("Temperaturas que cumplen la condición:", ciudad_A[dias_calientes])  # [18,20,22]

# Otra forma directa:
print("Días calientes (otra sintaxis):", temp[0][temp[0] > 16])

# -------------------------------------------------------------------
# 11. OPERACIONES VECTORIZADAS
# Cualquier operación aritmética se aplica elemento a elemento sin bucles.
# -------------------------------------------------------------------
# Convertir Celsius a Fahrenheit: F = C * 9/5 + 32
temp_fahrenheit = temp * 9/5 + 32
print("\nTemperaturas en Fahrenheit:\n", temp_fahrenheit)

# -------------------------------------------------------------------
# 12. NÚMEROS ALEATORIOS (PRNG moderno)
# Se recomienda usar np.random.default_rng() para proyectos serios.
# -------------------------------------------------------------------
rng = np.random.default_rng(seed=42)   # semilla para reproducibilidad
aleatorios_normal = rng.standard_normal((3,3))  # distribución normal estándar
aleatorios_uniforme = rng.uniform(0, 10, size=5)  # uniforme [0,10)
print("\nAleatorios normal (3x3):\n", aleatorios_normal)
print("Aleatorios uniforme [0,10):", aleatorios_uniforme)

# -------------------------------------------------------------------
# 13. UN POCO DE ÁLGEBRA LINEAL
# Producto punto y descomposiciones (imprescindibles en ML).
# -------------------------------------------------------------------
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
producto_punto = np.dot(A, B)          # o A @ B
print("\nProducto punto A·B:\n", producto_punto)

# Inversa de una matriz (si es invertible)
A_inv = np.linalg.inv(A)
print("Inversa de A:\n", A_inv)
print("A @ A_inv (identidad):\n", A @ A_inv)

# -------------------------------------------------------------------
# 14. RECOMENDACIONES FINALES DE ESTILO PROFESIONAL
# - Nombres de variables descriptivos.
# - Usa .copy() cuando necesites datos independientes.
# - Aprovecha las operaciones vectorizadas, evita bucles for.
# - Familiarízate con los métodos de agregación (sum, mean, std, etc.).
# - Lee la documentación oficial: https://numpy.org/doc/stable/
# -------------------------------------------------------------------
print("\n¡Todo listo! Ya manejas NumPy como un profesional.")