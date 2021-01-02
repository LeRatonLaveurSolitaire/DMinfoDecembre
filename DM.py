##Thomas Boulanger et Siméon Boyer  PSI*1


import math
import numpy as np
import random

## N particules de masse m, rayon R, dans un récipient linéique, carré ou cubique de coté L

##Q1 : p est tableau de numpy de dimension 1 à une case contenant un flottant compris entre 0 et L.
##Q2 : c est un tableau de numpy définit comme argument de la fonction possible.
##Q3 : la première case du tableau c est comparé aux bords du récipient - au rayon des sphères - pour voir si il n entre pas
##en contacte - n y a pas pénétration - avec les parois, si il y a contact, la position n est pas possible, on return False
##Q4 : on compare ensuite la position de la boule c avec toutes les autres boules pour voir si il
##n y a pas de collisions - pénétration - entres elles, si il y en a une, on return False, sinon on return True
##Q5 : la fonction possible vérifie qu il est possible de placer une particule sur la position c 
##Q6 : p = R + (L-2*R)* np.random.rand(1)         avec cette version, il n y a pas de collision - pénétration -
## possible avec les bords
##Q7 : la fonction possible revera toujours Fasle, car il est impossible deplacer une 4 ème 
## particule, la fonction va donc être bloquer dans une boucle while.
##Q8 : C = 1 + N * (2 + (2 + N*2 + 1) + 1) + 1 = 2N² +6N +2 = O(N²) - j aurais mis N/2*2 au lieu de N*2
##Q9 : 
res=[]
while len(res)<N:
    p = R + (L-2*R)* np.random.rand(1)
    if possible(p): res.append(p)
    else : res=[]
return res
##Q10 : 
def placement1Drapide(N,R,L):
    l= L-N*2*R
    res=[l*np.random.rand(1) for i in range(N)]     //on place N point sur le segement [0;l[
    res.sort()                                      //on trie la liste
    for i in range(N)                               //pour chaque point, on ajoute le rayon de la particule 
        res[i]+=R+i*2*R                             //ainsi que le décalage des autres particules
    return res
##Q11 : 1 + N*2 + 1 + N*3 + 1 = O(N) c est mieux que la situation précédente, plus rapide et sans boucle répétitive
##Q12 :  - fait? un histogramme continu? -
##Q13 :
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
 ##Q14 : Entre chaque choc ou rebond, la particule avance en ligne droite
 ##Q15 : lorque m1=m2, v1'=v2 et v2'=v1, chaque particule part dans la direction de l autre avec la vitesse de celle-ci
 ##       il y a un transfert d énergie entre les deux particules
 ##Q16 : lorsque m1<<m2, v1'= - v1 + 2*v2 v2'=v2 cette situation corrspond à un rebond contre une paroie - si v2=0 -
 ##/Q17 : 
         def vol(p,t):
            p[0]+=p[1]*t
 ##Q18 : 
         def rebond(p,d):
            p[1][d]=-p[1][d]
 ##Q19 : 
         def choc(p1,p2):
            p1[1],p2[1]=p2[1],p1[2]
 
 ##Q20
def tr(p,R,L):
    v=p[1]
    if v==0: return None
    if v>0:
        distance=L-p[0]-R
        return distance/v,0
    #else
    distance = p[0]-R
    return -distance/v,0

##21
def tc(p1,p2,R):
    e1,e2=p1[0],p2[0]
    v1,v2=p1[1],p2[1]
    if e2<e1:
        #la particule 1 est la particule la plus à gauche
        e1,e2=e2,e1
        v1,v2=v2,v1
    if v2-v1>=0: #les particules s'éloignent
        return None
    #else
    vapp=v1-v2 #vitesse d'approche
    distance=e2-e1
    return distance/vrel

##22
def ajoutEv(catalogue,e):
    i=len(catalogue)
    while catalogue[i][1]<e[1] and i>=0:
        i-=1
    catalogue.insert(i+1,e)

##23
def ajout1p(catalogue,i,R,L,particules):
    #étape 1 : création de e
    t,d=tr(particules[i],R,L) #t et d existent, car l'événement est supposé valide
    e=[True,t,i,None,d]
    #étape 2 : insersion dans la liste des événements
    L=[e]
    #on recommence pour toutes les collisions possibles
    for j in range(len(particules)):
        if j!=i:
            t=tc(particules[i],particules[j],R)
            e=[True,t,i,j,None]
            ajoutEv(catalogue,e)

##24
def initCat(particules,R,L):
    catalogue=[]
    for i in range(len(particules)):
        ajout1p(catalogue,i,R,L,particules)
    return catalogue

##25
#Pour deux particules quelconques i et j (j!=i), la fonction considère la collision entre i et j, et entre j et i. On considère donc deux fois chaque collision
##26
#on pose N le nombre de particules considérées.
#C(initCat)=1+N*C(ajout1p)+1
#   C(ajout1p)=C(tr)+2+1+(N-1)*(C(tc)+1+C(ajoutEv)+1
#       C(ajoutEv)=1+len(catalogue)3+1 (len(catalogue) au pire) ; et len(catalogue) = (N2)/2 = O(N*2) (en moyenne, passe N fois sur une liste de i éléments, i variant de 1 à N)
#       C(tr)=O(1) et C(tc)=O(1)
#   donc C(ajout1p)=O(N**2)
#donc C(initCat=O(N**3)
##27
#il faut optimiser en priorité ajoutEv. On pourrait l'optimiser par un algorithme de tri différent du tri par insersion. On peut remplir catalogue dans un ordre quelconque, puis le trier, par tri fusion par exemple.
##28
#Si une particule n'est pas à l'arrêt, alors l'événement rebond est valide pour cette particule.
#Si toutes les particules sont à l'arrêt, alors pour toutes les particules, rebond n'a pas lieu. De plus, pour deux particules quelconques i et j, on a vj-vi=0 donc la collision n'a pas lieu non plus.

##29
def etape(particules,e):
    for i in range(particules):
        particules[0]+=particules[1]*e[1]
    if i[3]==None:
        rebond(particules[e[2]],e[4])
    else:
        choc(particules[e[2]],particules[e[3]])

##30
def majCat(catalogue,particules,e,R,L):
    for i in range(len(catalogue)):
        if catalogue[i][2] in (e[2],e[3]) or catalogue[i][3] in (e[2],e[3]):
            catalogue[i][0]=False
        else:
            catalogue[i][1]-=e[1]
    ajout1p(catalogue,e[2],R,L,particules)
    if e[3]!=None:
        ajout1p(catalogue,e[3],R,L,particules)

##31
def simulation(bdd,d,N,R,L,T):
    particules=situationInitiale(d,N,R,L)
    catalogue=initCat(particules,R,L)
    t=0 #on utilise T comme minuteur et t comme chronomètre
    compteur=0
    while T>=catalogue[-1][1]: #tant qu'il reste assez de temps pour que prochain événement ait lieu
        e=catalogue.pop()
        t+=e[1]
        T-=e[1]
        etape(particules,e)
        enregistrer(bdd,t,e,particules)
        majCat(catalogue,particules,e,R,L)
        compteur+=1
    return compteur

##32
#Les doublons sont mis à l'état 'non valide'(False) suite à l'exécution de leur événement doublon.
##33
#Cette méthode agit sur majCat et sur simulation.
#   -majCat : L'algorithme est légèrement plus paride puisqu'on ne modifie plus le temps des listes, 
#   mais reste du même ordre de grandeur puisqu'on doit toujours inspecter les événements pour déterminer 
#   lesquels ne sont plus valides.
#   -simulation : La variable t n'est plus nécesaire, on enregistre le temps e[1] au lieu de t. On pourrait 
#   même définir enregistrer dans la variable t. De plus, T est fixe et garde sa valeur initiale, i.e le 
#   temps de simulation.
#Cette méthode ne change en rien la précision du résultat, et change la complexité de manière négligeable. 
#Cependant elle est mieux adaptée au problème rencontré : à titre personnel je trouve ça plus parlant 
#de faire avancer le temps plutôt que de faire reculer la date de déclenchement des événements.
