import numpy as np
from math import *

epsilon = 10**(-6)
over = 10.1**20

def derivative(f,x):
    dx = 10**(-9)
    def deriv(k):
        nx = np.array(x, dtype = np.longfloat)
        nx[k] = x[k]+dx
        return (f(nx)-f(x))/dx

    m = len(x)
    return np.array([deriv(i) for i in range(m)])

def compare(a: np.ndarray, b: np.ndarray):
    '''
    :param a: not empty
    :param b: not empty
    :return: True if every coordinate is equal else False
    '''
    if False in set(a==b):
        return False
    return True

def GradientDescent(f, vars = 2, maximum = False):
    if maximum:
        def reverse_sign(f):
            def newf(x):
                return -f(x)
            return newf
        f = reverse_sign(f)

    iters = 0
    g = 0.5
    x = np.array([0 for i in range(vars)])

    inter_res = []

    while g > epsilon:
        iters+=1

        nx = x - g * derivative(f, x)
        if f(nx)<f(x):
            x = nx
        else:
            g /= 2

        inter_res.append(x)

        if iters>20:
            #print(inter_res)
            repeats = 0
            for i in range(iters-1,iters-20,-1):
                if compare(inter_res[i],inter_res[i-1]):
                    repeats+=1
            if repeats==19:
                return ('Not exist',iters)

        if abs(f(x))>over:
            return ('Not exist',iters)
        if iters>10000:
            print('Cycled:',f,x0,maximum)
            #break



    return (x, iters)


def test(f, vars = 2, maximum=False):
    f_msg = 'max' if maximum else 'min'

    res = GradientDescent(f, vars=vars, maximum=maximum)
    if str(res[0]) == 'Not exist':
        if maximum:
            print('Maximum doesn\'t exist')
        else:
            print('Minimum doesn\'t exist')
    else:
        x = ''
        for i in range(vars-1): x+=str(res[0][i])+'; '
        x+=str(res[0][len(res[0])-1])

        print('x_{}:'.format(f_msg),x)
        print('f(x_{}) ='.format(f_msg),f1(res[0]))
        print('Iterations:',res[1])
    print()

if __name__ == '__main__':
    f1 = lambda x: 2*x[0]**2+3*x[1]**2-4*x[0]+5*x[1]-1
    x0 = (10,10)

    print('Task 1, Gradient descent method:\n')
    test(f1)
    test(f1,maximum=True)

    f2 = lambda x: x[0]**2+2*x[1]**2-4*x[1]**4-x[0]**4+3
    xs = [(10,10), (10, -10), (-10, 10), (-10, -10), (0,0)]

    print('Task 2, Gradient descent method:\n')
    test(f2)
    test(f2, maximum=True)

    print('Task 3, Gradient descent method:\n')
    f3 = lambda x: x[0]**2-x[1]**2
    test(f3)
    test(f3, maximum=True)

    print('Task 4, Gradient descent method:\n')
    def f4(x_):
        x,y,z = x_
        return (x**2+y**2+z**2)**2+((x-2)**2+(y-2)**2+(z-2)**2)**2

    test(f4, vars = 3)
    test(f4, vars = 3, maximum=True)
