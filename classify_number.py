# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    """Dado un número entero n, retorna True si es par, False si es impar."""
    return n % 2 == 0

def is_positive(n):
    """Dado un número entero n, retorna True si es mayor a 0, False en caso contrario."""
    return n > 0

# ---- Función a implementar ----

def classify_number(n):
        
    """
    Dado un número entero n, retorna un string que lo clasifica.
    Debe USAR las funciones is_even e is_positive para resolver el ejercicio.

    Clasificaciones posibles:
      - "positive even"   (positivo y par)
      - "positive odd"    (positivo e impar)
      - "negative even"   (negativo y par)
      - "negative odd"    (negativo e impar)
      - "zero"            (el número es 0)
    """
    
    n_even = is_even(n)
    n_pos = is_positive(n)
   
    if n == 0:
        return "zero"
    
    elif n_even and n_pos:
        return "positive even"
    
    elif n_even and not n_pos:
        return "negative even"
    
    elif not n_even and not n_pos:
        return "negative odd"
    
    elif n_pos and not n_even:
        return "positive odd" 
    

n = int(input())

print(classify_number(n))