from fractions import Fraction
import numpy as np

#lista = np.array([1, 2, 3, 4], dtype=object)
lista = np.array([1, 2, 3, 4])

def leer_escalar(mensaje="Escalar: "):
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

def leer_fila(mensaje="Número de fila: "):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: introduce un número entero válido.")
#Nos devuelve el numero de la fila

def procesar_escalar(escalar, list):
    lista_Frac = list.astype(object)
    return escalar * lista_Frac
#Aplica una operacion a la lista

def definir_fila_y_escalar():
    fila = leer_fila()
    escalar_original = leer_escalar()
    escalar_procesado = procesar_escalar(escalar_original, lista)
    
    print(f"Escalar original: {escalar_original} (tipo {type(escalar_original).__name__})")
    print(f"Escalar procesado (multiplicado por 2/3): {escalar_procesado} (tipo {type(escalar_procesado).__name__})")
    
    return fila, escalar_procesado

# Ejecución
if __name__ == "__main__":
    fila, escalar = definir_fila_y_escalar()
    print(f"\nResultado final: fila = {fila}, escalar = {escalar}")