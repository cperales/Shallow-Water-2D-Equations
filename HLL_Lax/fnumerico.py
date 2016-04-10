# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 11:58:24 2014

@author: carlos
"""
import HLL as fhll
import flax as flax
import numpy as np

def fnumerico(U0, Z, dx, pt):

    longitud=len(U0[0,:])
    DU=np.zeros([2,longitud])
#    Tengamos en cuenta que "cotadt" tiene que incluir ahora la diagonalización del jacobiano del flujo
    maxautovalor=1e-02
    for i in range(0,longitud-1):
        u = abs(U0[1,i]/(U0[0,i]+1e-08)*(U0[0,i]>=1e-03))
        h = U0[0,i]
        autovalor = u + np.sqrt(9.8*h)
        if maxautovalor < autovalor:
            maxautovalor = autovalor

    cfl = 0.9
    cotadt = cfl*dx/maxautovalor

    if cotadt>pt:
        cotadt=pt
    dth = float(cotadt/dx)

    #Ahora se recorren las interceldas.
    #La primera y la ultima las se tratan de forma distinta
    #Pues les falta una celda al lado
    #Dependiendo de las condiciones de contorno o del esquema
    #con el que queramos resolver, se comentan/descomentan las siguientes líneas
	
    hdt = float(dx/cotadt)

    Ui=U0[:,0]
    Ui[1]=0.18
    
    dmas,dmen = fhll.HLL(Ui,U0[:,0],Z[0],Z[0])
#    dmas,dmen = flax.flax(Ui,U0[:,0],Z[0],Z[0],hdt)
    DU[:,0]+= dmas

    
    for i in range(0,longitud-1):
        fInterdmas,fInterdmen=fhll.HLL(U0[:,i],U0[:,i+1],Z[i],Z[i+1])
#        fInterdmas,fInterdmen=flax.flax(U0[:,i],U0[:,i+1],Z[i],Z[i+1],hdt) 
        DU[:,i]+=fInterdmen
        DU[:,i+1]+=fInterdmas

    Uf=U0[:,longitud-1]
    Uf[0]=0.33

    dmas,dmen = fhll.HLL(U0[:,longitud-1],Uf,Z[longitud-1],Z[longitud-1])
#    dmas,dmen = flax.flax(U0[:,longitud-1],Uf,Z[longitud-1],Z[longitud-1],hdt) 
    DU[:,longitud-1]+= dmen
    
    U0[:,:]=U0-dth*DU  
    for i in range(0,longitud-1):
        if U0[0,i]<1.e-3:
            U0[0,i]=0
            U0[1,i]=0
    return U0,cotadt