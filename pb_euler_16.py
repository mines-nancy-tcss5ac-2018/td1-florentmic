# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def solve(n):
    """Solve the 16th Euler problem.

    Return the sum of the digits of a binar number.
    """
    val=0
    for chiffre in str(n):
        val+=int(chiffre)
        
    return val
    

        
    
assert solve(2**15)==26

print(solve(2**1000))




