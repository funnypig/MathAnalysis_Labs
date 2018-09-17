from math import *

EPSILON = 10**(-12)

dx = 0.000001

def f1(x):
    return x**10-0.1*x-0.01

def f2(x):
    return 6*sin(x**7)+x**21-6*x**14

def derivative(x0, f):
    return (f(x0+dx)-f(x0-dx))/(2*dx)

def DoubleSplitMethod(a,b,f):
    c = (a+b)/2

    iters = 0

    while abs(f(c)) > EPSILON:
        if f(c)<0:
            a = c
        else:
            b = c
        c = (a+b)/2

        iters+=1

    return (c,f(c),iters)

def SecantMethod(a, b, f):
    x = [a,b]
    while abs(f(x[-1]))>EPSILON:
        x.append(
            x[-1] - f(x[-1]) * (x[-1]-x[-2]) / (f(x[-1])-f(x[-2]))
        )

    return (x[-1],f(x[-1]),len(x))

def TangentMethod(a,b,f):
    x = [a]
    while abs(f(x[-1]))>EPSILON:
        x.append(
            x[-1] - f(x[-1]) / derivative(x[-1],f)
        )
    return (x[-1],f(x[-1]),len(x))

if __name__ == '__main__':
    print('Метод половинного поділу:\n')

    res = DoubleSplitMethod(0,1,f1)
    print('Function: x**10-0.1*x-0.01')
    print('f('+str(res[0])+') = '+str(res[1])+' ~ 0')
    print('Operations made:',res[2])

    print()

    res = DoubleSplitMethod(-0.4,0.6,f2)
    print('Function: 6*sin(x**7)+x**21-6*x**14')
    print('f('+str(res[0])+') = '+str(res[1])+' ~ 0')
    print('Operations made:',res[2])

    print('\nМетод січних:\n')

    res = SecantMethod(0, 1, f1)
    print('Function: x**10-0.1*x-0.01')
    print('f('+str(res[0])+') = '+str(res[1])+' ~ 0')
    print('Operations made:',res[2])

    print()

    res = SecantMethod(-0.4, 0.6, f2)
    print('Function: 6*sin(x**7)+x**21-6*x**14')
    print('f('+str(res[0])+') = '+str(res[1])+' ~ 0')
    print('Operations made:',res[2])

    print('\nМетод дотичних:\n')

    res = TangentMethod(0, 1, f1)
    print('Function: x**10-0.1*x-0.01')
    print('f('+str(res[0])+') = '+str(res[1])+' ~ 0')
    print('Operations made:',res[2])

    print()

    res = TangentMethod(-0.4, 0.6, f2)
    print('Function: 6*sin(x**7)+x**21-6*x**14')
    print('f('+str(res[0])+') = '+str(res[1])+' ~ 0')
    print('Operations made:',res[2])
