from math import *
import numpy as np
from numpy.random import randint as rand

EPSILON = 10**(-9)
dx = 0.000001

def derivative(x0, f):
    return (f(x0+dx)-f(x0-dx))/(2*dx)

def Th1(a,b,f):
    l = 0.5
    x0 = (a+b)/2
    x1 = f(x0)
    iters = int(log(EPSILON*(1-l)/abs(x0-x1), l))+1

    for i in range(iters):
        x1 = f(x1)

    return (x1, iters)

def Th2(a,b,f):
    m = derivative(a, f)
    M = derivative(b, f)
    l = 1/(2*m)

    _lambda = 1-m/(2*M)
    x0 = b
    x1 = x0 - l*f(x0)
    iters = int(log(EPSILON * (1-_lambda) / abs(x0 - x1), _lambda))+1

    for i in range(iters):
        x1 = x1 - l*f(x1)

    return (x1, iters)

def Th3_a(m, show_arrays = False):
    c = np.array([rand(-500,500)/10000 for i in range(m*m)]).reshape((m,m))
    b = np.array([np.random.sample()*10*((-1)**(1+rand(-2,2))) for i in range(m)])
    a = c+np.eye(m,m)

    def f(x):
        return a@x+b-x

    l = np.sqrt(np.sum([ci**2 for ci in c.flat]))
    x0 = b*l
    x1 = f(x0)

    n = int(log(EPSILON*(1-l)/np.sqrt(np.sum((x0[i]-x1[i])**2 for i in range(m))), l))+1

    for i in range(n):
        x1 = f(x1)

    if show_arrays:
        print('C:',c)
        print('b:',b)

    print('3a) MSE(error):',np.sum(
        (x1[i]-b[i])**2 for i in range(m)
        )/m
    )

    return (x1, n)

def Th3_b(m, show_arrays = False):
    c = np.fromfunction(lambda i,j: 0*(i+j)+rand(-100,100)/10000, (m,m))
    b = np.array([np.random.sample()*10*((-1)**(1+rand(-2,2))) for i in range(m)])
    a = c+np.eye(m,m)

    def f(x):
        return a@x+b-x

    l = np.sqrt(np.sum([ci**2 for ci in c.flat]))
    x0 = np.zeros(m)
    x1 = f(x0)

    n = int(log(EPSILON*(1-l)/abs(np.sum(x1-x0)), l))+1

    for i in range(n):
        x1 = f(x1)

    if show_arrays:
        print('C:',c)
        print('b:',b)

    print('3b) MSE(error):',np.sum(
        (x1[i]-b[i])**2 for i in range(m)
        )/m
    )

    return (x1, n)


if __name__ == '__main__':

    f1 = lambda x: 0.5*cos(x)
    res = Th1(-10,10,f1)
    print('Task 1:')
    print('x =',res[0])
    print('f('+str(res[0])+') =',f1(res[0]))
    print('Iterations:',res[1])

    print()

    f2 = lambda x: x**5-x-1
    res = Th2(1,2, f2)
    print('Task 2:')
    print('x =',res[0])
    print('F('+str(res[0])+') =',f2(res[0]))
    print('Iterations:',res[1])

    print()

    print('Task 3.a:\n')
    res = Th3_a(10, show_arrays = False)
    print('Iterations:',res[1])

    print()

    print('Task 3.b:\n')
    res = Th3_b(80, show_arrays = False)
    print('Iterations:',res[1])
