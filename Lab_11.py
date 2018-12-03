from math import *

''' 
Task 1:
Length: 2.265016445647299

Task 2:
Length: 9.417111117717473
Mass: 101.19958302420733

Task 3:
Length: 9.417111117717473
Mass: 0.017251954173590846
B =  4

Process finished with exit code 0

'''

def Integral(f, a, b):
    n = 10**5
    step = (b-a)/n
    int_sum = 0
    x = a

    for i in range(n-1):
        int_sum += 0.5*(f(x)+f(x+step))*step
        x+=step

    return int_sum

def CurveLength(a,b, u:list):
    dx = 10**(-6)
    def derivative(f,t):
        return 0.5*(f(t+dx)-f(t-dx))/dx

    def d(x):
        res = 0
        for ui in u:
            res+=derivative(ui,x)**2
        return sqrt(res)

    return Integral(d, a, b)

def CurveMass(a,b,u,r):
    dx = 10**(-6)
    def derivative(f,t):
        return 0.5*(f(t+dx)-f(t-dx))/dx

    def d(x):
        res = 0
        for ui in u:
            res+=derivative(ui,x)**2
        return sqrt(res)

    def f(x):
        p = [ui(x) for ui in u]
        return r(p)*d(x)


    return Integral(f, a, b)


if __name__ == '__main__':
    u1 = lambda t: e**t
    u2 = lambda t: cos(t)
    u3 = lambda t: t**7

    print('Task 1:')
    l = CurveLength(0, 1, [u1,u2,u3])
    print('Length:',l)
    print()

    print('Task 2:')
    u1 = lambda t: t
    u2 = lambda t: log(t,e)
    r = lambda x: x[0]+e**(x[1])
    l = CurveLength(1, 10, [u1,u2])
    m = CurveMass(1,10,[u1,u2],r)

    print('Length:',l)
    print('Mass:',m)
    print()

    print('Task 3:')
    # lazy implementation
    eps = 10**(-5)

    u1 = lambda t: t
    u2 = lambda t: e**(t)
    r = lambda x: e**(-4*x[0])

    b = 2
    m = CurveMass(1, b, [u1,u2], r)
    while True:
        nm = CurveMass(1,b+1, [u1,u2], r)
        if abs(nm-m)<eps:
            break
        else:
            m = nm
            b+=1

    print('Length:',l)
    print('Mass:',CurveMass(1,b,[u1,u2],r))
    print('B = ',b)
