from math import *

eps = 10**(-9)
inf = 10**9

def IntegralTrapezium(a,b,n,f, fragmentation = None):
    '''
    Calculate Integral from a to b using trapezium method
    :param a: lower bound
    :param b: upper bound
    :param n: number of trapeziums
    :param f: function under the integral
    :fragmentation: function to calculate i-th point
    :return: calculated integral
    '''
    x = [a+(b-a)*i/n for i in range(n+1)] if fragmentation is None else [fragmentation(a,b,n,i) for i in range(n+1)]
    return sum( [ (f(x[i])+f(x[i+1]))/2*(x[i+1]-x[i]) for i in range(n) ] )


if __name__ == '__main__':
    fragm_wider = lambda a, b, n, i: a + ((b - a) * i ** 2) / n ** 2
    fragm = lambda a, b, n, i: b - ((b-a)*(n-i)**2)/n**2

    print('Task 1.1:\n')
    f1 = lambda x: e**(-x**2)
    A = log(1 / eps, e)

    res = IntegralTrapezium(0, A, 1000, f1, fragm_wider)
    wolfram = sqrt(pi)/2

    print('n = 1000')
    print('Result:',res)
    print('Difference:',abs(res-wolfram))

    print()

    res = IntegralTrapezium(0, A, 1000, f1, fragm_wider)

    print('n = 10000')
    print('Result:',res)
    print('A =',A)
    print('Difference:',abs(res-wolfram))

    print('\nTask 1.2:\n')
    f2 = lambda x: sin(x)/(x**2+1)
    A = tan((pi / 2) - eps*10**6)

    res = IntegralTrapezium(0, A, 1000, f2, fragm_wider)
    wolfram = 0.646761

    print('n = 1000')
    print('Result:',res)
    print('A =',A)
    print('Difference:',abs(res-wolfram))

    print()

    res = IntegralTrapezium(0, A, 10000, f2, fragm_wider)
    
    print('n = 10000')
    print('Result:',res)
    print('A =',A)
    print('Difference:',abs(res-wolfram))

    print('\nTask 1.3:\n')
    f3 = lambda x: sin(x)/sqrt(1-x)
    A = 1.0 - eps

    res = IntegralTrapezium(0, A, 1000, f3, fragm)
    wolfram = 1.18698444477923899

    print('n = 1000')
    print('Result:',res)
    print('A =',A)
    print('Difference:',abs(res-wolfram))

    print()

    res = IntegralTrapezium(0, A, 10000, f3, fragm)

    print('n = 10000')
    print('Result:',res)
    print('A =',A)
    print('Difference:',abs(res-wolfram))
