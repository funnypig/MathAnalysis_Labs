from math import *
import time

'''
    16 sec execution... so output:
    
Polynoms multiplication:

N = 100
Usual: 0.01795196533203125
Fourier: 0.18450403213500977
N = 1000
Usual: 1.8650124073028564
Fourier: 14.763518571853638


Long multiplication:

Python multiplication: 0.0
Fourier multiplication: 0.5315778255462646
'''

def Transform(coefs):
    tc = []
    N = len(coefs)

    for n in range(N):
        c = 0
        for k in range(N):
            c += coefs[k] * e  ** complex(0, -2*pi*k*n/N)

        tc.append(c)

    return tc

def RevTrans(values):
    v =values
    rtc = []
    N = len(values)

    for n in range(N):
        fn = 0

        for k in range(N):
            fn += v[k] * e ** complex(0, 2*pi*k*n/N)
        fn/=N

        rtc.append(fn)

    return rtc

def Fourier_PolynomMultiplication(coefs1, coefs2):
    N = max(len(coefs2),len(coefs1))*2

    while len(coefs1)!=N: coefs1.append(0)
    while len(coefs2)!=N: coefs2.append(0)

    coefs1 = Transform(coefs1)
    coefs2 = Transform(coefs2)

    coefs = [coefs1[i] * coefs2[i] for i in range(len(coefs1))]

    coefs = RevTrans(coefs)

    coefs = [round(c.real) for c in coefs]

    while coefs[-1] == 0 and len(coefs)>1:
        coefs.pop()

    return coefs

def FourierLongMult(number1, number2):
    number1.reverse()
    number2.reverse()

    m = Fourier_PolynomMultiplication(number1, number2)

    number = ''

    left = 0
    for i in range(len(m)):
        m[i] += left
        left = m[i]//10
        m[i] %= 10

        number = str(m[i]) + number

    while left != 0:
        m.append(left%10)
        left//=10
        number = str(m[-1])+number

    return (m,number)

def UsualPolynomMult(coefs1, coefs2):
    coefs = [0 for i in range(len(coefs2)*len(coefs1)+1)]

    for i1, c1 in enumerate(coefs1):
        for i2, c2 in enumerate(coefs2):
            coefs[i1+i2] += c1*c2

    while coefs[-1] == 0:
        coefs.pop()

    return coefs

def CheckTime(f, *args):
    st = time.time()
    res = f(*args)
    fin = time.time()

    return {'result':res, 'time':fin-st}

if __name__ == '__main__':
    print('Polynoms multiplication:\n')
    c1 = [i for i in range(1,101)]
    c2 = [i for i in range(100,0, -1)]

    m = CheckTime(Fourier_PolynomMultiplication,c1,c2)
    m2 = CheckTime(UsualPolynomMult, c1, c2)

    print('N = 100')
    print('Usual:',m2['time'])
    print('Fourier:',m['time'])

    c1 = [i for i in range(1,1001)]
    c2 = [i for i in range(1000,0, -1)]

    m = CheckTime(Fourier_PolynomMultiplication,c1,c2)
    m2 = CheckTime(UsualPolynomMult, c1, c2)

    print('N = 1000')
    print('Usual:',m2['time'])
    print('Fourier:',m['time'])

    print('\n')
    print('Long multiplication:\n')

    # build numbers 123...9899100 and vice versa
    n1_poly = [i for i in range(1,10)]
    n2_poly = [1,0,0]

    for i in range(10,100):
        n1_poly.append(i//10)
        n1_poly.append(i%10)
    for i in range(99,9,-1):
        n2_poly.append(i//10)
        n2_poly.append(i%10)

    n1_poly.extend([1,0,0])
    n2_poly.extend([i for i in range(9,0,-1)])

    # build usual ints
    int_n1 = int(str(n1_poly).replace(' ','').replace(',','')[1:-1])
    int_n2 = int(str(n2_poly).replace(' ','').replace(',','')[1:-1])


    t1 = CheckTime(lambda x,y: x*y, int_n1, int_n2)
    t2 = CheckTime(FourierLongMult, n1_poly, n2_poly)

    print('Python multiplication:',t1['time'])
    print('Fourier multiplication:',t2['time'])
