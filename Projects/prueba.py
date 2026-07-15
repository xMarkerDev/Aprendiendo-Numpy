import numpy as np      
        
def despeje(number_str):
  num, den = number_str.split('/', 1)   # separa numerador y denominador
  numerador = int(num)
  denominador = int(den)
  
  elemento = "2/3"
  en, ed = elemento.split('/', 1)
  elemento_numerador = int(en)
  elemento_denominador = int(ed)
  
  if elemento_denominador == denominador:
    elemento_nuevo = numerador
    print(f"Este es el elemento despejado, solo queda el numerador: {elemento_nuevo}")
  else:
    elemento_nuevo = f"{(elemento_numerador * numerador)}/{elemento_denominador * denominador}"
  print(f"Este es el elemento no despejado: {elemento_nuevo}")
  print(type(elemento_nuevo))
  return elemento_nuevo  
        
def procesar(number):
  if isinstance(number, str):
    escalar = despeje(number)
    print(f"Este es nuestro escalar ya multiplicado o despejado: {escalar}")
  elif isinstance(number, int):
    escalar = number
  return escalar

def definir_fila_y_escalar():
    while True:
        try:
            fila = int(input("Número de fila: "))
            entrada = input("Escalar: ").strip()
            
            # Si el usuario escribe una fracción (contiene '/')
            if '/' in entrada:
                num, den = entrada.split('/', 1)   # separa numerador y denominador

                if den == "0":
                    print("Error: el denominador no puede ser cero.\n")
                    continue
                es = f"{num}/{den}"
            else:
                es = int(entrada)   # entero o decimal normal
            
            escalar = procesar(es)
            
            print(type(escalar))
            print(escalar)
            return fila, escalar
        except ValueError:
            print("Error: introduce valores numéricos válidos. Para fracciones usa 'a/b'.\n")
  

#Despeje
                 
definir_fila_y_escalar()