from Measures import MeasureCalculation
from random import randint
from math import sin, cos, pi

'''
    Output:
    
    Task 1:
    4.8027443906250005

    Task 2:
    2.89731025

    Task 3:
    [0.09000707373046875, 0.08978979663085938, 0.05764317504882813]
'''

def Integral(f, _set, start_point, fin_point):
    steps = 2**4
    dim_ranges = [[start_point[i]*steps,fin_point[i]*steps] for i in range(len(start_point))]

    greater_set_measure = 1
    for i in range(len(start_point)):
        greater_set_measure *= abs(fin_point[i]-start_point[i])

    n = 10**6
    points_in_set = 0
    sum_fx = 0

    for i in range(n):
        point = []
        for k in range(len(start_point)):
            d = randint(dim_ranges[k][0], dim_ranges[k][1])/steps
            point.append(d)

        if _set(point):
            points_in_set += 1
            sum_fx += f(point)

    mA = points_in_set * greater_set_measure / n

    integral = sum_fx * mA / points_in_set

    return integral

def MassCenter(f, _set, start_point, fin_point):
    point = []

    for i in range(len(start_point)):
        def fx(x):
            res = f(x)
            res *= x[i]
            return res
        point.append(Integral(fx, _set, start_point, fin_point))

    return point


if __name__ == '__main__':

    def Task_1():
        _set = lambda x: x[0]**4+x[1]**4 <= 1
        p = lambda x: 2-x[0]**2-x[1]**2

        print('Task 1:')
        print(Integral(p, _set, [-1,-1], [1,1]))
        print()

    def Task_2():
        _set = lambda x: x[0]**2+x[1]**2<=1 and abs(x[2])<=2
        p = lambda x: x[0]**2+x[1]**2

        print('Task 2:')
        print(4*Integral(p, _set, [0,0,0],[1,1,2]))
        print()

    def Task_3():
        _set = lambda x: x[0]**2+x[1]**2+x[2]**2<=1 and x[0]>=0 and x[1]>=0 and x[2]>=0
        p = lambda x: x[0]**2+x[1]**2
        center = MassCenter(p, _set, [0,0,0], [1,1,1])

        print('Task 3:')
        print(center)


    def Task_4(): # IT DOES NOT WORK YET
        _set = lambda x: x[0]**2*(cos(x[1])**4+sin(x[1])**4+cos(x[2])**2+sin(x[2])**2+2)<=1
        p = lambda x: x[1]**2+x[2]**2

        x = lambda s: s[0]*sin(s[1])*cos(s[2])
        y = lambda s: s[0]*sin(s[1])*sin(s[2])
        z = lambda s: s[0]*cos(s[1])

        _set = lambda p: _set([x(p), y(p), z(p)])
        p = lambda _p: p([x(_p), y(_p), z(_p)])

        fp = [1, pi, 2*pi]
        center = Integral(p, _set, [0,0,0], [x(fp), y(fp), z(fp)])

        print('Task 4:')
        print(center)

    Task_4()
