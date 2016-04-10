# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 11:58:24 2014

@author: carlos
"""
# FiniteVolume4
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
import fnumerico as lx

# Si en animation se usa blit=True hay que utilizar lo siguiente
# para que los textos del titulo se actualicen
#try:
#    from parche import _blit_draw
#    anim.Animation._blit_draw = _blit_draw
#except ImportError:
#    print 'ImportError: No module named parche'
###############################################################

#def condIni(x): # Test 1
#    U0 = np.zeros([2,len(x)])
#    U0[0,:] = 4.0 # Esta componente será h
#    U0[1,:] = 10.0 # Esta componente será q=h*u
#    Z = 0.48*(1-((x-20)/4)**2)*(x>=16)*(x<=24) # Esta componente será el fondo
#    return U0,Z

def condIni(x): # Test 2
    U0 = np.zeros([2,len(x)])
    U0[0,:] = 0.33 # Esta componente será h
    U0[1,:] = 0.18 # Esta componente será q=h*u
    Z = (0.2-0.05*(x-10)**2)*(x>8)*(x<12)+0.0 # Esta componente será el fondo
    return U0,Z
    

#def condIni(x): # Test 3
#    U0 = np.zeros([2,len(x)])
#    U0[1,:] = -350.0*(x<50.0/3.0)+350.0*(x>=50.0/3.0) # Esta componente será q=h*u
#    Z = 1*(x>(25.0/3.0))*(x<12.5)+0.0 # Esta componente será el fondo
#    U0[0,:] = 10.0-Z # Esta componente será h
#    return U0,Z    

a=0.0
b=25.0
n=125
h=float(b-a)/float(n)
print 'Discretización del espacio utilizada =', h

t0=0.0
t1=40.0
pasos=1.5*(t1-t0)
pt=(t1-t0)/pasos
print 'Paso de tiempo utilizado =', pt

intercelda=np.arange(a,b,h)

celdas = np.arange(a+h/2,b-h/2,h)
U0,Z = condIni(celdas)


t=0
nextTime=0

fig = plt.figure()
ax = plt.axes(xlim=(a, b), ylim=(0.0, 0.5)) # eta
#ax = plt.axes(xlim=(a, b), ylim=(0.0, 3.0)) # Froude
#ax = plt.axes(xlim=(a, b), ylim=(0.0, 0.4)) # caudal


l, = ax.plot([], [], lw=2)
time_text=ax.set_title('t=0')
ax.plot(celdas,Z)

def animate(j, celdas, U0, Z, h, pt):
    global t,nextTime
    
    while t<nextTime:
        U0,dt = lx.fnumerico(U0, Z, h, nextTime-t)
        t+=dt
        print t    

    eta = U0[0,:] + Z[:]
##    print eta
#    u = np.zeros(len(U0[0,:]))
#    u = U0[1,:]/(U0[0,:]+1e-08)*(U0[0,:]>=1e-03)
#    v = abs(u)/np.sqrt(9.81*(U0[0,:]+1e-08))*(U0[0,:]>=1e-03)
    
    nextTime+=pt
     
    ax.set_title('t=%3.2f'%t)

    l.set_data(celdas,eta)
#    l.set_data(celdas,U0[1,:])
#    l.set_data(celdas,v)

    
    return l,time_text



def init():
    l.set_data([],[])
    time_text.set_text('')
    return l,time_text


#Para guardar la pelicula:
ani = anim.FuncAnimation(fig, animate, np.arange(0,pasos+1), fargs=(celdas, U0, Z, h, pt),init_func=init, blit=False, repeat=False)
#ani.save('./HLL_test2_eta.mp4',writer='mencoder',fps=15)
ani.save('./Lax_test2_eta.mp4',writer='mencoder',fps=30)

plt.show()