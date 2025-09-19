#function to take integer as arg and return even for even and odd for odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
 #transform a number to a string:
def number_to_string(num):
    return f"{num}"
            
            
#remove spaces
def no_space(x):
    return x.replace(" ", "")