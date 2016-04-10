# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:18:57 2015

@author: carlos
"""
#F4
import numpy as np

def F(U) :
    u = U[1]/(U[0]+1e-8)*(U[0]>=1e-3) # La velocidad

    F = np.zeros(2)

    F[0] = U[1]
    F[1] = 9.81*0.5*U[0]**2+u*U[1]
    return F