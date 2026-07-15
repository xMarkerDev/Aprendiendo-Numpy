from fractions import Fraction
import numpy as np

def sol_Escalar(mensaje="Escalar: "):
    while True:
        entrada = input(mensaje).strip() #Solicitamos El escalar por el cual multiplicar la fila y eliminamos los espacios
        if '/' in entrada: #Si el escalar contiene la notacion (a/b)
            try:
                num_str, den_str = entrada.split('/', 1) #Separamos el escalar en dos partes con respecto al "/"
                num = int(num_str) #Primera parte es el numerador entero
                den = int(den_str) #Segunda parte es el denominador entero
                if den == 0:
                    print("Error: el denominador no puede ser cero.")
                    continue
                return Fraction(num, den) #Retornamos los valores enteros en forma fraccionada
            except ValueError:
                print("Error: formato inválido. Usa 'a/b' con números enteros.")
        else:
            try:
                return Fraction(int(entrada), 1) #Si el escalar no contiene la notacion (a/b) lo transformamos a fraccion a/1
            except ValueError:
                print("Error: introduce un número entero o una fracción 'a/b'.")
#Nos devuelve el escalar fraccionado

def sol_Numero_De_Fila(mensaje="Número de fila: "):
    while True:
        try:
            return int(input(mensaje)) #Solicitamos un valor para el numero de filas, lo convertimos a entero y lo retornamos
        except ValueError:
            print("Error: introduce un número entero válido.")
#Nos devuelve el numero de la fila

def operacion_Es_Fil(esc, fil): #Solicitamos el escalar y la lista (mas especifico la fila a multiplicar)
    fil_Frac = fil.astype(object) #Convertimos esta lista a un type object para realizar operaciones fraccionadas
    return esc * fil_Frac #Retornamos la operacion escalar x lista
#Aplica una operacion a la lista

#Formatear la fila completa para convertirla en un string
def formatear_array_fracciones(arr):
    # Convierte cada elemento a string en formato "num/den" si es Fraction, o str() si no
    return '[' + ' '.join(f"{x.numerator}/{x.denominator}" if isinstance(x, Fraction) else str(x) for x in arr) + ']'


def definir_Matriz_Escalar(matriz_Nueva):
    n_fila = sol_Numero_De_Fila() #Defininimos nuestro numero de fila
    n_escalar = sol_Escalar() #Definimos nuestro numero de escalar
    
    matriz = matriz_Nueva.copy()
    
    matriz[n_fila-1] = operacion_Es_Fil(n_escalar, matriz[n_fila-1])
    return matriz

def resultado(matriz):
    matriz_String = formatear_array_fracciones(matriz)
    print(f"Matriz Frac: {matriz}")
    print(f"Matriz String: {matriz_String}")
    
# def resultado(n_fila, n_escalar, matriz):
#     fila_Formateada = formatear_array_fracciones(fila_Nueva)
#     print(f"Fila Nueva Principal: {fila_Nueva}")
#     print(f"Fila Nueva String: {fila_Formateada}") #  (tipo {type(fila_Nueva).__name__})
#     print(type(fila_Formateada))