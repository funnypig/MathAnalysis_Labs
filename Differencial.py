from math import *
from itertools import permutations
import numpy as np

dx = 10**(-6)
eps = 10**(-6)

def partial_derivative(f, x, pos):
    nx = np.array(x, dtype = np.longfloat)
    nx[pos] = x[pos]+dx
    return (f(nx)-f(x))/dx

def vec_derivative_1(f,x):
    m = len(x)
    return np.array([partial_derivative(f,x,[i]) for i in range(m)])

def vec_derivative_2(f,x):
    res = 0
    for i in range(len(x)):
        nf = lambda x: vec_derivative_1(f,x)
        for j in range(len(x)):
            res += partial_derivative(nf,x,j)
    return res

# fail:
def vec_derivative_3(f,x):
    res = 0
    for i in range(len(x)):
        nf = lambda x: vec_derivative_1(f,x)
        for j in range(len(x)):
            nnf = lambda x: vec_derivative_1(nf,x)
            for k in range(len(x)):
                res += partial_derivative(nnf,x,k)
    return res


def Taylors_Formula(f,x,x0):
    res = f(x0)+vec_derivative_1(f,x0)@(x-x0)+vec_derivative_2(f,x0)@(x-x0)**2/2
    return res


if __name__ == '__main__':
    f = lambda x: x[0]**5*log(1+x[1], e)
    x = np.array([[1.5,0.7],[1.05,0.07],[1.005,0.007]])
    x0 = np.array([1,0])

    for i in range(len(x)):
        r = Taylors_Formula(f,x[i], x0)
        print('Task 1.{}:\nf(x)='.format(i+1),\
              f(x[i]),'\nResult:',r,'\nDifference:',f(x[i])-r,'\n')

    f = lambda x: e**(x[0]+x[1]+x[2])
    x = np.array((0.1,0.05,-0.01))
    x0 = np.array([-eps*100,-eps*100,-eps*100])

    found = False
    for i in range(200):
        for j in range(200):
            for k in range(200):
                x0 =  np.array([-eps*100+eps*(i+1),-eps*100+eps*(j+1),-eps*100+eps*(k+1)])
                r = Taylors_Formula(f,x,x0)

                if abs(f(x)-r)<=0.1:
                    found = True
                    break
            if found:break
        if found:break

    print('Task 2:\nf(x)=',f(x),'\nResult:',r,'\nDifference:',f(x)-r,'\nx0 =',x0,'\n')

    f = lambda x: x[0]**2+x[1]**4


    f = lambda x: (x[0]-x[1]+1)*sin(x[0]+x[1])
    x = np.array([0.1,0.05])
    x0 = np.array([0,0])
    print('Task 4:\nf(x)=',f(x),'\nResult:',r,'\nDifference:',f(x)-r,'\n')
