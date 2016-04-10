# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 14:22:05 2014

@author: carlos
"""
# flax2
import numpy as np
import F as F

def flax(UL,UR,zl,zr,hdt) :

    dmas = np.zeros(2)
    dmen = dmas
    g = 9.8

    ul = UL[1]/(UL[0]+1e-8)*(UL[0]>=1e-3)+0.0 # La velocidad de la celda UL
    ur = UR[1]/(UR[0]+1e-8)*(UR[0]>=1e-3)+0.0 # La velocidad de la celda UR

    alfa0=hdt
    alfa1=0
            
# Hallamos entonces D+ y D- en i+1/2
    difz = zr - zl
    vecdifz = [difz,0]
    
    t = g*(UL[0]+UR[0])*0.5*difz
    vect = [0,t]
    
    dmas = 0.5*alfa0*(UR-UL+vecdifz)  + 0.5*(1+alfa1)*(F.F(UR)-F.F(UL) + vect)
    dmen = -0.5*alfa0*(UR-UL+vecdifz)  + 0.5*(1-alfa1)*(F.F(UR)-F.F(UL) + vect)

    return dmas,dmen