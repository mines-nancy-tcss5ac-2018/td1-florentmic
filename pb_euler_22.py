# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:32:54 2018

@author: michon8u
"""

def solve():
    """Solve the 22th Euler problem.

    Return the total score of a list of name.
    """
    f = open('p022_names.txt', 'r')
    prenoms=str(f.readlines())
    prenoms=prenoms.split('","')
    prenoms[0]=prenoms[0][3:]
    prenoms[-1]=prenoms[-1][:-3]
    prenoms.sort()
    print(prenoms)
    
    
    scores=[] #facultatif
    score_total=0
    
    
    longueur=len(prenoms)
    for i in range(longueur):
        val=0
        for lettre in prenoms[i]:
            val+=ord(lettre)
        score=val*(i+1)
        scores.append(score) #facultatif
        score_total+=score
        
    f.close()
    
    return(score_total)
        
        

print(solve())



