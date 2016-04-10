# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 14:22:05 2014

@author: carlos
"""
def fgodunov(ul,ur) : 
    if ul>=ur: #Choque
        s = 0.5*(ul+ur)
        if s>=0:
            z = ul**2/2
            return z
        else:
            z = ur**2/2
            return z
        
    else: #Onda de rarefacción
        if ur<0:
            z = ur**2/2
            return z
        elif ul<0 and ur>0:
            z = 0
            return z
        elif ul>0:
            z = ul**2/2
            return z