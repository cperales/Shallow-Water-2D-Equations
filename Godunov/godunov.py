# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 11:58:24 2014

@author: carlos
"""
# Godunov9

import fgodunov as fg
import numpy as np

def godunov(U0, h, pt):
    cfl=0.9
    longitud=len(U0)

    DU=np.zeros(longitud)
    
    #Du[i] Va a corresponder al incremento que vamos a hacer
    #Du[i] ---> F_{i+1/2}-F_{i-1/2}    
    
    Umax=max(U0)
    
    #Ahora vamos a recorrer las interceldas.
    #La primera y la ultima las trato de forma distinta
    #Pues les falta una celda al lado

    #Primera y última celda -> duplico el estado (CC de frontera libre)

    DU[0]=-fg.fgodunov(U0[0],U0[0])
    
    for i in range(0,longitud-1):
        fIntercelda=fg.fgodunov(U0[i],U0[i+1])
        DU[i]+=fIntercelda
        DU[i+1]-=fIntercelda
        

    DU[longitud-1]+=fg.fgodunov(U0[longitud-1],U0[longitud-1])
        
   
    cotadt = cfl*h/Umax

    if cotadt>pt:
        cotadt=pt
    dth = float(cotadt/h)
    
    U0[:]=U0-dth*DU    
    
    return U0,cotadt