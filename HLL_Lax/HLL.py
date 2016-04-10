# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 14:22:05 2014

@author: carlos
"""
# HLL4
import numpy as np
import F as F

def HLL(UL,UR,zl,zr) :
    dmas = np.zeros(2)
    dmen = dmas
    g = 9.8

    ul = UL[1]/(UL[0]+1e-8)*(UL[0]>=1e-3)+0.0 # La velocidad de la celda UL
    ur = UR[1]/(UR[0]+1e-8)*(UR[0]>=1e-3)+0.0 # La velocidad de la celda UR

    c_1 = ul-np.sqrt(9.8*UL[0])
    c = ur-np.sqrt(9.8*UR[0])
    if c < c_1 :
        c_1 = c

    c_2 = ul+np.sqrt(9.8*UL[0])
    c = ur+np.sqrt(9.8*UR[0])
    if c > c_2 :
        c_2 = c
            
    if (abs(c_2-c_1)>1.e-8):
        alfa0 = (c_2*abs(c_1)-c_1*abs(c_2))/(c_2-c_1)
        alfa1 = (abs(c_2)-abs(c_1))/(c_2-c_1)
    else:
        alfa0=0.0
        alfa1=0.0
            
# Hallamos entonces D+ y D- en i+1/2
    difz = zr - zl
    vecdifz = [difz,0]
    
    t = g*(UL[0]+UR[0])*0.5*difz
    vect = [0,t]
    
    dmas = 0.5*alfa0*(UR-UL+vecdifz)  + 0.5*(1+alfa1)*(F.F(UR)-F.F(UL) + vect)
    dmen = -0.5*alfa0*(UR-UL+vecdifz)  + 0.5*(1-alfa1)*(F.F(UR)-F.F(UL) + vect)

    return dmas,dmen