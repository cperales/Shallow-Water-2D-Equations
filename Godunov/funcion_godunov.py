# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 11:58:24 2014

@author: carlos
"""
# Godunov9
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as anim
import godunov as g

# Si en animation se usa blit=True hay que utilizar lo siguiente
# para que los textos del titulo se actualicen
#try:
#    from parche import _blit_draw
#    anim.Animation._blit_draw = _blit_draw
#except ImportError:
#    print 'ImportError: No module named parche'
###############################################################


def condIni(x): # Choque
    U0=2.0*(x<=5.0)+0.5*(x>5.0)
    return U0
    
#def condIni(x): # Rarefacción
#    U0=0.5*(x<=5.0)+2.0*(x>5.0)
#    return U0    
    
a=0
b=20
n=50
h=float(b-a)/float(n)
print 'Discretización del espacio utilizada =', h


t0=0.0
t1=20.0
pasos=50
pt=(t1-t0)/pasos
print 'Paso de tiempo utilizado =', pt

intercelda=np.arange(a,b,h)


celdas = np.arange(a+h/2,b-h/2,h)
U0=condIni(celdas)

t=0
nextTime=0

fig = plt.figure()
ax = plt.axes(xlim=(a, b), ylim=(0, 2.5))

l, = ax.plot([], [], lw=2)
time_text=ax.set_title('t=0')



def animate(j, celdas, U0, h, pt):
    global t,nextTime
    
    while t<nextTime:
        U0,dt = g.godunov(U0, h, nextTime-t)
        t+=dt
        
    
    nextTime+=pt
     
    ax.set_title('t=%3.2f'%t)

    l.set_data(celdas,U0)
    
    return l,time_text



def init():
    l.set_data([],[])
    time_text.set_text('')
    return l,time_text
    


#Para guardar la pelicula:
ani = anim.FuncAnimation(fig, animate, np.arange(0,pasos+1), fargs=(celdas, U0, h, pt),init_func=init, blit=False, repeat=False)
ani.save('./Godunov_Choque2.mp4',writer='mencoder',fps=10)
#ani.save('./Godunov_Rarefacción.mp4',writer='mencoder',fps=10)

plt.show()