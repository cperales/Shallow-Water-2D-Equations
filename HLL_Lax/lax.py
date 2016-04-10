# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 11:58:24 2014

@author: carlos
"""
# lax3

import flax as fl
import numpy as np

def lax(U0, h, pt):
    longitud=len(U0[0,:])
    DU=np.zeros([2,longitud])
    # Por escoger una de las filas de la matriz; lo mismo daría otra fila
    #Du[i] Va a corresponder al incremento que vamos a hacer
    #Du[i] ---> F_{i+1/2}-F_{i-1/2}
    #Tengamos en cuenta que "cotadt" tiene que incluir ahora la diagonalización del jacobiano del flujo
    maxautovalor=0.001
    for i in range(0,longitud-1):
        u = abs(U0[1,i]/U0[0,i])
        h = abs(U0[0,i])
        autovalor = u + np.sqrt(9.8*h)
        if maxautovalor < autovalor:
            maxautovalor = autovalor

    cfl = 0.9
    cotadt = cfl*h/maxautovalor
    
    if cotadt>pt:
        cotadt=pt
    dth = float(cotadt/h)
    hdt = float(h/cotadt)
    
    #Ahora vamos a recorrer las interceldas.
    #La primera y la ultima las trato de forma distinta
    #Pues les falta una celda al lado

    #Primera celda (duplico el estado) -> condiciones de contorno
    #Aun no lo hemos visto

    DU[:,0]-=fl.flax(U0[:,0],U0[:,0],hdt)
    
    for i in range(0,longitud-1):
        fIntercelda=fl.flax(U0[:,i],U0[:,i+1],hdt)
        DU[:,i]+=fIntercelda
        DU[:,i+1]-=fIntercelda
        
        
    #Ultima celda (duplico el estado) -> condiciones de contorno
    #Aun no lo hemos visto    
    DU[:,longitud-1]+=fl.flax(U0[:,longitud-1],U0[:,longitud-1],hdt)    



    
    U0[:,:]=U0-dth*DU    
    
    return U0,cotadt