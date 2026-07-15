#Codigo de practica para aplicar mi aprendizaje en numpy

import numpy as np

print(f"Version: {np.__version__}")

#Funcion para el selector de operaciones

def menu():
  print("Selecciona Una Operacion a Realizar")
  print("1. Cambiar Filas")
  print("2. Multiplicar por un Escalar")
  print("3. Sumar Filas")
  print("4. Mostrar Matriz")
  print("5. Salir")

matriz = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9],
                   [10,11,12],
                   [13,14,16],
                   [17,18,19],
                   ])

fils_n = matriz.size
matriz_Resultante = []

#Cambio de Filas

def cambio_De_Filas(m, f1, f2):  
  fila_1 = m[f1-1,:]
  fila_2 = m[f2-1,:]
  
  nueva_matriz = m[0:fils_n].copy()
  
  nueva_matriz[f1-1] = fila_2
  nueva_matriz[f2-1] = fila_1
  
  return nueva_matriz

  
#cambio_De_Filas(matriz,6,2)

#Multiplicacion por un escalar

def multiplicacion_De_Fila(m, f1, escalar):
  print("Realizando una multipicacion por escalar")
  
  fila_1 = m[f1-1,:]
  
  nueva_matriz = m[0:fils_n].copy()
  
  nueva_matriz[f1-1] = fila_1 * escalar
  
  print(f"Matriz original: {m}")
  print(f"Matriz cambiada: {nueva_matriz}")
  
#multiplicacion_De_Fila(matriz, 4, 50)

#Suma de Filas

def Suma_De_Filas(m, f1, f2):
  print("Realizando una Suma de Filas")
  
  fila_1 = m[f1-1,:]
  fila_2 = m[f2-1,:]
  
  nueva_matriz = m[0:fils_n].copy()
  
  nueva_matriz[f1-1] = fila_1 + fila_2
  
  print(f"Matriz original: {m}")
  print(f"Matriz cambiada: {nueva_matriz}")

#Suma_De_Filas(matriz, 1, 2)

#Creacion de matriz aleatoria

def crear_Matriz(n, m):
  rng = np.random.default_rng(seed=42)
  matriz_Aleatoria = rng.integers(low=0, high=10, size=(n,m))
  return matriz_Aleatoria

#Definir Dimensiones de la matriz

def definir_Dimension():
  while True:
    try:
      filas = int(input("Ingresa el numero de Filas: "))
      columnas = int(input("Ingresa el numero de Columnas: "))
      return filas, columnas
    except ValueError:
      print("Error: Ingresa numeros validos")

#Definir Filas 1 y 2

def definir_Filas():
  while True:
    try:
      fila_1 = int(input("Ingresa la fila 1: "))
      fila_2 = int(input("Ingresa la fila 2: "))
      return fila_1, fila_2
    except ValueError:
      print("Error: Ingresa numeros validos")

#Definir filas y escalar

def definir_Fila_Escalar():
  while True:
    try:
      fila_1 = int(input("Ingresa la Fila 1: "))
      escalar = int(input("Ingresa el Escalar: "))
      return fila_1, escalar
    except ValueError:
      print("Error: Ingresa numeros validos")

#Empezamos con el codigo
filas, columnas = definir_Dimension()

matriz_Nueva = crear_Matriz(filas, columnas)
print(f"Esta es la nueva matriz: {matriz_Nueva}")

while True:
  menu()
  option = input("Elige una opcion del 1-5: ")
  
  if option == "5":
    print("Gracias por usar mi codigo")
    break
  
  elif option == "4":
    if matriz_Resultante:
      print("Matriz resultante")
      print("operacion.pop")
    else:
      print("No hay operaciones en el historial")
  
  elif option in ["1", "2", "3"]:
    
    if option == "1":
      fila_1, fila_2 = definir_Filas()
      resultado = cambio_De_Filas(matriz_Nueva, fila_1, fila_2)
      print(resultado)
      
    el
