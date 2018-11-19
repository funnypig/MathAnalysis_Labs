import random
from math import sin, e

'''
spheres: 2 - 0.7853981633974483
3 - 0.5235987755982988
4 - 0.30842513753404244
5 - 0.16449340668482262
'''

''' m-dimensional sphere measure calculation
Spheres:
Dimensions: 1
1.0 

Dimensions: 2
0.737648 

Dimensions: 3
0.48435 

Dimensions: 4
0.281094 

Dimensions: 5       # previous results n = 6; this one n = 4
0.110128 

6 - memory error. implementation fail 
'''

'''
Task 1:

{'2 dimension': 1, 'n': 4, 'Result': 4.20703125, 'E (error)': 1.515625}
{'2 dimension': 1, 'n': 6, 'Result': 3.874267578125, 'E (error)': 0.4306640625}
{'2 dimension': 1, 'n': 8, 'Result': 3.7560577392578125, 'E (error)': 0.11346435546875}
{'2 dimension': 1, 'n': 10, 'Result': 3.721188545227051, 'E (error)': 0.029270172119140625}
{'2 dimension': 1, 'n': 12, 'Result': 3.71160227060318, 'E (error)': 0.0074651241302490234}

B: 3.208324 

Task 1.2:

{'3 dimension': 1, 'n': 4, 'Result': 2.945556640625, 'E (error)': -2.11181640625}
{'3 dimension': 1, 'n': 6, 'Result': 1.9577751159667969, 'E (error)': -0.5408706665039062}

B: 1.473624 


Integral:
A (n=4): 1.9280348999831571
A (n=6): 2.066811986431364
B (n=100): 2.0362326286320784
B (n=1000): 2.0171491273514763
B (n=10000): 1.9778935959683506
'''



def MeasureCalculation(n: int, _set, dims: int, start_point, fin_point):
    '''
        Передбачається, що А вже лежить у брусі start_point->fin_point
    '''
    point = start_point
    step = 1/2**n

    def dim_calc(point, k):
        '''
        Обчислює точки, по k-му виміру. точки в інших вимірах фіксовані
        '''
        p = point[k]
        new_points = [point]
        while p<=fin_point[k]:
            np = point.copy()
            np[k] = p

            new_points.append(np)

            if k+1!=dims:
                new_points.extend(dim_calc(np, k+1))

            p+=step

        return new_points

    A = dim_calc(point, 0)

    pts = 10**6
    in_set = 0

    for i in range(10**6):
        p = random.choice(A)
        if _set(p):
            in_set+=1

    v = [abs(fin_point[i]-start_point[i]) for i in range(dims)]
    MQ0 = 1
    for i in v:
        MQ0 *= i

    # TODO: do not calculate whole set A. just pick up point from  it randomly by coordinates

    return (in_set/pts)*MQ0

def MeasureCalculation_3Dim(n: int, _set, start_point, fin_point):
    def points(x):
        points = []
        step = 1/2**(n-1)
        for i in range(-1,2):
            for j in range(-1,2):
                for k in range(-1,2):
                    points.append((x[0]+i*step,x[1]+j*step,x[2]+k*step))
        return points
    def define_position_Intersect(x, _points = None):
        if _points is None: _points = points(x)
        return _set(x) and {_set(p) for p in _points} == {True}

    def define_position_In(x, _points = None):
        if _points is None: _points = points(x)
        return _set(x) or  (True in set([_set(p) for p in _points]))


    N = 0
    N_in = 0

    step = 1/2**n

    i = start_point[0]
    while i <= fin_point[0]:
        j = start_point[1]
        while j<=fin_point[1]:
            k = start_point[2]
            while k<=fin_point[2]:
                if define_position_Intersect((i,j,k)):
                    N+=1
                if define_position_In((i,j,k)):
                    N_in += 1
                k+=step
            j+=step
        i+=step

    return {'3 dimension':1,'n':n,'Result':N_in*(1/2**n)**3,'E (error)':(N-N_in)*(1/2**n)**3}

def MeasureCalculation_2Dim(n: int, _set, start_point, fin_point):
    def define_position_Intersect(x):
        step = 1/2**(n-1)
        return _set(x) or _set((x[0]-step,x[1]-step)) or _set((x[0]-step,x[1]+step)) or\
               _set((x[0]+step,x[1]+step)) or _set((x[0]+step,x[1]-step))
    def define_position_In(x):
        step = 1/2**(n-1)
        return _set(x) and _set((x[0]-step,x[1]-step)) and _set((x[0]-step,x[1]+step)) and\
               _set((x[0]+step,x[1]+step)) and _set((x[0]+step,x[1]-step))

    N = 0
    N_in = 0

    i = start_point[0]
    while i <= fin_point[0]:
        j = start_point[1]
        while j<=fin_point[1]:
            if define_position_Intersect((i,j)):
                N+=1
            if define_position_In((i,j)):
                N_in += 1

            j+=1/2**n
        i+=1/2**n

    return {'2 dimension':1,'n':n,'Result':N_in*(1/2**n)**2,'E (error)':(N-N_in)*(1/2**n)**2}


def Integral_2d(f,n, _set, start_point, fin_point):
    step = 1/2**n
    def define_position_In(x):
        return _set(x) and _set((x[0]-step,x[1]-step)) and _set((x[0]-step,x[1]+step)) and\
               _set((x[0]+step,x[1]+step)) and _set((x[0]+step,x[1]-step))

    s = 0
    mq = (1/(2**n))**2

    i = start_point[0]
    while i<=fin_point[0]:
        j = start_point[1]
        while j<=fin_point[1]:
            if define_position_In((i,j)):
                s += f((i,j)) * mq

            j+=step
        i+=step
    return s

def Integral_2d_B(f, n, _set, start_point, fin_point):
    def define_position_In(x):
        return _set(x) and _set((x[0]-step,x[1]-step)) and _set((x[0]-step,x[1]+step)) and\
               _set((x[0]+step,x[1]+step)) and _set((x[0]+step,x[1]-step))

    ma = MeasureCalculation(4, _set, 2, start_point, fin_point)

    step = 1/2**4
    x = []
    i = start_point[0]
    while i<=fin_point[0]:
        j = start_point[1]
        while j<=fin_point[1]:
            if define_position_In((i,j)):
                x.append((i,j))

            j+=step
        i+=step
    s = 0
    for i in range(n):
        s += f(random.choice(x))
    return ma*s/n

def MeasureCalc_2d_B(n: int, _set, start_point, fin_point):
    return MeasureCalculation(n, _set, 2, start_point, fin_point)
def MeasureCalc_3d_B(n: int, _set, start_point, fin_point):
    return MeasureCalculation(n, _set, 3, start_point, fin_point)


if __name__ == '__main__':
    # фунція визначає, чи знаходиться точка в множині
    set1 = lambda p: p[0]**4+p[1]**4 <= 1

    def Task1():
        print('Task 1:\n')
        print(MeasureCalculation_2Dim(4, set1, (-1,-1), (1,1)))
        print(MeasureCalculation_2Dim(6, set1, (-1,-1), (1,1)))
        print(MeasureCalculation_2Dim(8, set1, (-1,-1), (1,1)))

        print('\nB:',MeasureCalc_2d_B(4, set1, [-1,-1], [1,1]),'\n')

        print()

    set2 = lambda p: p[0]**2+p[1]**2<=1 and p[0]+p[1]<=p[2]<=2*p[1]+3*p[2]

    def Task12():
        print('Task 1.2:\n')
        print(MeasureCalculation_3Dim(4, set2, (-1,-1,0), (1,1,1)))
        print(MeasureCalculation_3Dim(6, set2, (-1,-1,0), (1,1,1)))

        print('\nB:',MeasureCalc_3d_B(4, set2, [-1,-1,0], [1,1,1]),'\n')

    def Task2():
        f = lambda x: sin(e**(x[0]-x[1]))
        _set = lambda p: p[0]**4+p[1]**4 <= 1

        print('Integral:')
        print('A (n=4):',Integral_2d(f, 4, _set, (-1,-1), (1,1)))
        print('A (n=6):',Integral_2d(f, 6, _set, (-1,-1), (1,1)))

        print('B (n=100):',Integral_2d_B(f,100, _set, [-1,-1], [1,1]))
        print('B (n=1000):',Integral_2d_B(f,1000, _set, [-1,-1], [1,1]))
        print('B (n=10000):',Integral_2d_B(f,10000, _set, [-1,-1], [1,1]))

    Task2()

    # Launch yourself
    s_set = lambda p: sum([x**2 for x in p]) <= 0.25
    '''
    print('Spheres:')
    for i in range(1,7):
        print('Dimensions:',i)
        res = MeasureCalculation(5, s_set, i, [-0.5 for k in range(i)], [0.5 for k in range(i)])
        print(res,'\n')
    '''
