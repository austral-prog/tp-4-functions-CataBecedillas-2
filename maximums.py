# Replace the "ANSWER HERE" for your answer

def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
   
    max2 = max(x, y) #usas la inegrada "max" la cual automatixamente calcula el maximo entre dos variables.
                     #pones entre parentesis las variables a comparar.
    
    return max2 #le pedis a la funcion que te devuelva cual es el maximo.


def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
   
    max3 = max_of_two(x, y) #haces una nueva variable que te diga como salio lo de arriba.
                            
  
    max4 = max(max3, z) #con esa informacion lo comparas con la z.
    return max4 #le pedis a la funcion que te devuelva cual es el maximo entre los tres.

#x = int(input())
#y = int(input()) #le pones input a las variables.
#z = int(input())

#print(max_of_two(x, y))       #llamas a la funcion
#print(max_of_three(x, y, z))