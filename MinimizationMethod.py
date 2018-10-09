import numpy as np
from math import *

from Differencial import vec_derivative_1, vec_derivative_2

epsilon = 10**(-6)
over = 10.1**20

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

        nx = x - g * vec_derivative_1(f, x)
        if f(nx)<f(x):
            x = nx
        else:
            g /= 2

        inter_res.append(x)

        if abs(f(x))>over:
            return ('Not exist',iters)
        if iters>10000:
            print('Cycled:',f,x0,maximum)
            #break

    return (x, iters)

def NewtonsMethod(f,x0, maximum = False):
    if maximum:
        def reverse_sign(f):
            def newf(x):
                return -f(x)
            return newf
        f = reverse_sign(f)

    x = x0

    iters = 0
    while True:
        iters+=1

        nx = x - 1/(vec_derivative_2(f,x))*vec_derivative_1(f,x)

        if f(nx)>f(x) or abs(f(nx)-f(x))<epsilon:
            break

        x=nx

    if iters == 1:
        return('Not exist',iters)
    return (x,iters)

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

def testN(f, x0, maximum=False):
    f_msg = 'max' if maximum else 'min'

    res = NewtonsMethod(f, x0, maximum=maximum)
    if str(res[0]) == 'Not exist':
        if maximum:
            print('Maximum doesn\'t exist')
        else:
            print('Minimum doesn\'t exist')
    else:
        x = ''
        for i in range(len(res[0])-1): x+=str(res[0][i])+'; '
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

    print("Newton's method:\n")
    print('Task 1:')
    testN(f1, (10,10))
    testN(f1, (10,10), True)

    print('Task 2:\n')
    testN(f1, (10,10))
    testN(f1, (10,10), True)

    xs = [(10,10), (10, -10), (-10, 10), (-10, -10), (0,0)]

    for i in range(len(xs)):
        testN(f2, xs[i])
        testN(f2, xs[i], True)

    print('Task 3:\n')
    testN(f3, (1,1))
    testN(f3, (1,1), maximum=True)

    print()
    print('Task 4:\n')
    for x in [(1,1,1),(3,3,3),(-1,-2,-3)]:
        testN(f4, x)
        testN(f4, x, maximum=True)
