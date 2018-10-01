from math import *

EPS = 10**(-9)

def derivative(f, x0, pos):
    return (f(x0[pos]+EPS)-f(x0[pos]-EPS))/(2*EPS)

def diff(f,x:tuple):
    df = 0
    for i in range(len(x)):
        df += derivative(f,x,i)
    return df

def calculate(f : staticmethod, x : tuple, x0 : tuple):
    fact = 1
    fx = f(x)
    LEN = len(x)
    add = fx
    i = 1
    while add > EPS:
        add = diff(f,x)*(sum([x[k]-x0[k] for k in LEN]))**i/fact

        i+=1
        fact*=i

if __name__ == '__main__':
    f = lambda x: x[0]**5*log(1+x[1], e)
    r = calculate(f, (1.5, 0.7), (1,0))
    print(r)
