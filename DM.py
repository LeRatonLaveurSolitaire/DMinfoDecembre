//Thomas Boulanger et Siméon Boyer  PSI*1


import math
import numpy as np
import random

// N particules de masse m, rayon R, dans un récipient linéique, carré ou cubique de coté L

//Q1 : p est tableau de numpy de dimension 1 à une case contenant un flottant compris entre 0 et L.
//Q2 : c est un tableau de numpy définit comme argument de la fonction possible.
//Q3 : la première case du tableau c est comparé aux bords du récipient pour voir si il n entre pas
//en contacte avec les parois, si il y a contact, la position n est pas possible, on return False
//Q4 : on compare ensuite la position de la boule c avec toutes les autres boules pour voir si il
//n y a pas de collisions entres elles, si il y en a une, on return False, sinon on return True
//Q5 : la fonction possible vérifie qu il est possible de placer une particule sur la position c 
//Q6 : p = R + (L-2*R)* np.random.rand(1)         avec cette version, il n y a pas de collision
// possible avec les bords
//Q7 : la fonction possible revera toujours Fasle, car il est impossible deplacer une 4 ème 
// particule, la fonction va donc être bloquer dans une boucle while.
//Q8 : C = 1 + N * (2 + (2 + N*2 + 1) + 1) + 1 = 2N² +6N +2 = O(N²)
//Q9 : 
res=[]
while len(res)<N:
    p = R + (L-2*R)* np.random.rand(1)
    if possible(p): res.append(p)
    else : res=[]
return res
//Q10 : 
def placement1Drapide(N,R,L):
    l= L-N*2*R
    res=[l*np.random.rand(1) for i in range(N)]     //on place N point sur le segement [0;l[
    res.sort()                                      //on trie la liste
    for i in range(N)                               //pour chaque point, on ajoute le rayon de la particule 
        res[i]+=R+i*2*R                             //ainsi que le décalage des autres particules
    return res
//Q11 : 1 + N*2 + 1 + N*3 + 1 = O(N) c est mieux que la situation précédente, plus rapide et sans boucle répétitive
//Q12 : 
//Q13 :
 def deplacement(D,N,R,L):
     def possible(c):
        for i in range(res):
            d = 0
            for j in ragne(D):
                d+=(c[j]-res[i][j])**2
            if d < R**2 :
                return False
        return True
     res = []
     While len(res)<N:
        p = R + (L-2*R)* np.random.rand(D)
        if possible(p) : res.append(p)
        else : res=[]
     return res
 //Q14 : Entre chaque choc ou rebond, la particule avance en ligne droite
 //Q15 : lorque m1=m2, v1'=v2 et v2'=v1, chaque particule part dans la direction de l autre avec la vitesse de celle-ci
 //       il y a un transfert d'énergie entre les deux particules
 //Q16 : lorsque m1<<m2, v1'= - v1 + 2*v2 v2'=v2 cettesituation corrspond à un rebond contre une paroie
 //Q17 : def vol(p,t):
            p[0]+=p[1]*t
 //Q18 : def rebond(p,d):
            p[1][d]=-p[1][d]
 //Q19 : def choc(p1,p2):
            p1[1],p2[1]=p2[1],p1[2]
       
