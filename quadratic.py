# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = ((b**2) - (4*a*c))
    quadratic1 = (-b + (((discriminante)** (1/2)))) / (2*a)
    quadratic2 = (-b - (((discriminante)** (1/2)))) / (2*a)
   
    if discriminante > 0:
        return f"({quadratic1}, {quadratic2})"
    
    elif discriminante == 0:
        return f"({quadratic1})"
    
    elif discriminante < 0:
        return "( )"
    
    
def value_y(a, b, c, x):
    fx = a*(x**2) + b*x + c

    return int(fx)


def to_string(a, b, c):
    funcion = f"f(x) = {int(a)} * X^2 + {int(b)} * X + {int(c)}"
    lineal = f"f(x) = {int(b)} * X + {int(c)}"
    b_cero = f"f(x) = {int(a)} * X^2 + {int(c)}"
    
    if a == 0 and b != 0:
        return lineal
    elif b == 0 and a != 0:
        return b_cero
    elif a == 0 and b == 0:
        return f"f(x) = {int(c)}"
    else:     
        return funcion

def derivation(a, b, c):
    derivada = f"{2* int(a)} * X + {int(b)}"
    b_cero = f"{2* int(a)} * X"
    
    if a == 0 and b != 0:
        return f"f'(x) = {int(b)}"
    
    elif b == 0 and a !=0:
        return f"f'(x) = {b_cero}"
    
    elif b == 0 and a == 0:
        return f"f'(x) = 0"
    else:
        return f"f'(x) = {derivada}"

#a = float(input())
#b = float(input())
#c = float(input())
#x = int(input())

#print(roots(a, b, c))
#print(value_y(a, b, c, x))
#print(to_string(a, b, c))
#print(derivation(a, b, c))