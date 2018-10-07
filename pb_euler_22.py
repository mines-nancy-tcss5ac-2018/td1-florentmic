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
    prenoms[0]=prenoms[0][3:] # Supprime un '[', un '"' et un '/' du premier prénom, restants à cause du séparateur choisi.
    prenoms[-1]=prenoms[-1][:-3] # Supprime un '[', un '"' et un '/' du dernier prénom, restants à cause du séparateur choisi.
    prenoms.sort()    
    
    score_total=0
    
    for i,prenom in enumerate(prenoms,1):  # on commence l'indexation à 1
        val=0 # compte le score lié aux lettres du prénom
        for lettre in prenom:
            val+=ord(lettre)-64  # on retire 64 pour que la valeur de A soit 1, celle de B soit 2, etc..
        score=val*(i)  # multiplication du score du prénom par sa position dans la liste de prénoms classée
        score_total+=score
        
    f.close() #fermeture du fichier
    
    return(score_total)
        
        

print(solve())



