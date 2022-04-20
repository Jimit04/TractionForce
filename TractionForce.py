# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:37:43 2021

@author: rajgunvavy
"""

from scipy.integrate import nquad as DI
from math import sqrt

# Geometric and Model details
m = 40980   #kg
G = 2300    #mm Track Guage
l = 1021    #mm CG from left
r = 1279    #mm CG from right

# Track Patch
a = 3370    #mm Track Length
b = 500     #mm Track Width

# Constants
g = 9.810   #m/s2
mus = 0.9   #Coefficient of static friction
muk = 0.1   #Coefficient of rolling friction

# Reaction force
Rl = m*g*r/(l+r) 
Rr = m*g*l/(l+r)

#Rolling friction force
Fl = muk*Rl
Fr = muk*Rr

def fl(x,y):
    fl = mus*(Rl/(a*b))*sqrt(x**2 + y**2)
    return fl

def fr(x,y):
    fr = mus*(Rr/(a*b))*sqrt(x**2 + y**2)
    return fr

# Representing right turn, Left track forward, Right Track Support

Msl,errl = DI(fl,[[-a/2,a/2],[-b/2,b/2]])   #Static moment resistance due left
Msr,errr = DI(fr,[[-a/2,a/2],[-b/2,b/2]])   #Static moment resistance due right
Mrl = Fl*G                                  #Rolling moment resistance due left
Mrr = Fr*0                                  #Rolling moment resistance due right

M = Msl + Msr + Mrl + Mrr

Tl = (M/G) + Fl

print (Tl-Fl)
print (Tl)
print (M,Msl,Msr)




