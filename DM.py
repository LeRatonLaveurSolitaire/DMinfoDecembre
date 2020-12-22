# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:29:26 2020

@author: Thomas
"""
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
//Q6 : p = R + (L-2*R)* random()
