from math import *
from Integrals import IntegralSimpson

import numpy as np

''' 
    f'(t) = k0 f(t) + g(t)
    f(t0) = f0

    f'(t) = k f(t)
    f(t) = C e^(kt)
    C'(t)e^(kt) + C(t)ke^(kt) = k C(t) e^(kt) + g(t)
    C(t) = integral ( g(t)*e^(-kt) dt ) 
    
    C(t) = integral [t0 -> t] (g(s) e^(-ks) ds) + f0
    
    f(x0) = y0, f(x1) = y1, ..., f(xn) = yn
    
    (y[k+1]+y[k])/d = k0*y[k]+g(xk)
    
    y[k+1] = y[k] + d( k0 * y[k] + g(xk) ) 
'''

dx = 0.000001

def der(x0, f):
    return (f(x0+dx)-f(x0-dx))/(2*dx)

def gt(g, k, f0):
    def newg(t):
        nonlocal k, f0
        return g(t)*e**(-k*t)+f0
    return newg

def DiffEq(t0,t1, k0, f0, g, n = 10**3):
    x = [t0+i*(t1-t0)/n for i in range(n)]

    global dx
    dx = (t1-t0)/n

    def ft(t):
        nonlocal t0, n, g, k0, f0
        return IntegralSimpson(t0,t,n, gt(g,k0, f0)) * e**(k0*t)

    y = [f0]

    for i in range(1,n):
        y .append( y[-1] + dx* (k0 * y[-1] + g(x[i])) )

    plt.plot(x, [i**3 for i in x])
    plt.plot(x,y)
    plt.show()

    return y

def g(x):
    return 3*(x**2)-2*(x**3)

DiffEq(0,3,2,0,g)
