# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:09:19 2018

@author: michon8u
"""

def solve():
    """
    Solve the 55th Euler problem.
    Evalue the number of Lychrel number below ten-thousand..
    """
    number_of_Lychrel_number=0 
    
    for i in range (1,10000):
        
        i+=rev(i) # A palyndrom maybe a Lychrel number, so we must do the first addition before the WHILE loop.
        increment=1 # Not 0, because we already did an addition.
        
        while not isPalyndrom(i): 
        
            if increment<50:
                i+=rev(i)
                increment+=1
            else:
                number_of_Lychrel_number+=1
                break # quit the WHILE loop
                
    return(number_of_Lychrel_number)
    
        
def rev(n):
    """
    Returns the reversed number.
    For example rev(12345) will return 54321
    """
    return int(str(n)[::-1])
    

def isPalyndrom(n): #check if n is a palyndrom
    return n==rev(n)
    

assert(isPalyndrom(4994))
print(solve())




