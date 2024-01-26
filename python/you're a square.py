# Given an integral number, determine if it's a square number:

def is_square(n):    
    for i in range(n+1):
        if (i*i == n):
             return True
    return False