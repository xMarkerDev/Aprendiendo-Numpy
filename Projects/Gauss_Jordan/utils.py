from fractions import Fraction

def sol_Escalar(mensaje="Escalar: "):
    """
    Solicita al usuario un número que puede ser entero o fracción (a/b).
    Retorna un objeto Fraction.
    """
    while True:
        entrada = input(mensaje).strip()
        if '/' in entrada:
            try:
                num_str, den_str = entrada.split('/', 1)
                num = int(num_str)
                den = int(den_str)
                if den == 0:
                    print("Error: el denominador no puede ser cero.")
                    continue
                return Fraction(num, den)
            except ValueError:
                print("Error: formato inválido. Usa 'a/b' con números enteros.")
        else:
            try:
                return Fraction(int(entrada), 1)
            except ValueError:
                print("Error: introduce un número entero o una fracción 'a/b'.")


def sol_Numero_De_Fila(mensaje="Número de fila: ", max_filas=None):
    """
    Solicita un número de fila (1-indexado).
    Si se proporciona max_filas, valida que esté dentro del rango [1, max_filas].
    """
    while True:
        try:
            n = int(input(mensaje))
            if max_filas is not None and (n < 1 or n > max_filas):
                print(f"Error: el número debe estar entre 1 y {max_filas}.")
                continue
            return n
        except ValueError:
            print("Error: introduce un número entero válido.")