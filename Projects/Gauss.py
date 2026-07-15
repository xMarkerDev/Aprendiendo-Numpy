import numpy as np

print(f"Versión de NumPy: {np.__version__}\n")

#Operaciones
def cambio_de_filas(m, f1, f2):
    nueva = m.copy()
    nueva[[f1-1, f2-1]] = nueva[[f2-1, f1-1]]
    return nueva

def multiplicacion_de_fila(m, fila, escalar):
    nueva = m.copy()
    nueva[fila-1] = nueva[fila-1] * escalar
    return nueva

def suma_de_filas(m, f1, f2):
    nueva = m.copy()
    nueva[f1-1] = nueva[f1-1] + nueva[f2-1]
    return nueva

def crear_matriz(n, m):
    rng = np.random.default_rng(seed=42)
    return rng.integers(low=0, high=10, size=(n, m))

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

def definir_dos_filas():
    while True:
        try:
            f1 = int(input("Fila 1: "))
            f2 = int(input("Fila 2: "))
            return f1, f2
        except ValueError:
            print("Error: introduce números enteros.\n")

def definir_fila_y_escalar():
    while True:
        try:
            fila = int(input("Número de fila: "))
            entrada = input("Escalar: ").strip()
            
            # Si el usuario escribe una fracción (contiene '/')
            if '/' in entrada:
                num, den = entrada.split('/', 1)   # separa numerador y denominador
                numerador = float(num)
                denominador = float(den)
                if denominador == 0:
                    print("Error: el denominador no puede ser cero.\n")
                    continue
                escalar = numerador / denominador
            else:
                escalar = float(entrada)   # entero o decimal normal
                
            return fila, escalar
        except ValueError:
            print("Error: introduce valores numéricos válidos. Para fracciones usa 'a/b'.\n")

#Menu
def mostrar_menu():
    print("Operaciones para Gauss-Jordan")
    print("1. Cambiar filas")
    print("2. Multiplicar fila por escalar")
    print("3. Sumar filas")
    print("4. Mostrar matriz actual")
    print("5. Salir")

#Codigo Principal
filas, columnas = definir_dimension()
matriz_original = crear_matriz(filas, columnas)

matriz_actual = matriz_original.copy()

print("Matriz inicial:")
print(matriz_actual)

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-5): ").strip()

    if opcion == "5":
        print("¡Hasta luego!")
        break

    elif opcion == "4":
        print("\nEstado actual de la matriz:")
        print(matriz_actual)

    elif opcion in ("1", "2", "3"):
        # Verificar que la matriz tenga al menos 1 fila (siempre es cierto)
        if opcion == "1":
            f1, f2 = definir_dos_filas()
            if f1 < 1 or f1 > filas or f2 < 1 or f2 > filas:
                print("Número de fila fuera de rango.\n")
                continue
            matriz_actual = cambio_de_filas(matriz_actual, f1, f2)
            print("Filas intercambiadas. Nueva matriz:")
            print(matriz_actual)

        elif opcion == "2":
            fila, esc = definir_fila_y_escalar()
            if fila < 1 or fila > filas:
                print("Número de fila fuera de rango.\n")
                continue
            matriz_actual = multiplicacion_de_fila(matriz_actual, fila, esc)
            print(f"Fila {fila} multiplicada por {esc}. Nueva matriz:")
            print(matriz_actual)

        elif opcion == "3":
            f1, f2 = definir_dos_filas()
            if f1 < 1 or f1 > filas or f2 < 1 or f2 > filas:
                print("Número de fila fuera de rango.\n")
                continue
            matriz_actual = suma_de_filas(matriz_actual, f1, f2)
            print(f"Fila {f2} sumada a la fila {f1}. Nueva matriz:")
            print(matriz_actual)

    else:
        print("Opción no válida. Intenta de nuevo.")