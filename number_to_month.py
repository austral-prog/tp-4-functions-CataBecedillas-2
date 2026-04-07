# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    
    if month == 1:
        name1 = "enero"
    
    elif month == 2:
        name1 = "febrero"
    
    elif month == 3:
        name1 = "marzo"
        
    elif month == 4:
        name1 = "abril"
        
    elif month == 5:
        name1 = "mayo"   
    
    elif month == 6:
        name1 = "junio"
        
    elif month == 7:
        name1 = "julio"
    
    elif month == 8:
        name1 = "agosto"
    
    elif month == 9:
        name1 = "septiembre"
        
    elif month == 10:
        name1 = "octubre"
        
    elif month == 11:
        name1 = "noviembre"
        
    elif month == 12:
        name1 = "diciembre"
    
    else:
        return "error"
    
    return name1

month = int(input())


print(number_to_month(month))