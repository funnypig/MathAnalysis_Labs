import numpy as np
import matplotlib.pyplot as plt

''' Task 2 example output:

Robot position: 2.9997613422473135 ; 0.58533195395054
Lamps: [0.17033729 1.51565428 2.3959878  1.40338592 0.69114616] 
        [1.44331474 1.49489253 1.31185477 0.39083855 0.91026332]

Defined position: (3.0106078811595354, 0.5844063691115895, 0.009194138776982223)

'''

def Approximation(f, n, m, start, finish):
    x = np.linspace(start, finish, n)
    b = np.array([f(xi) for xi in x])
    b = b.transpose()
    A = np.array([[xi**j for j in range(m)] for xi in x])
    At = A.transpose()

    a = np.linalg.solve(At.dot(A), At.dot(b))

    polynom = lambda x: sum([a[i]*x**(i) for i in range(len(a))])

    return {'points':x,'result':a, 'polynom':polynom}

def Plot(f, start = 0, finish = 0, n = 1, points = None):
    x = None
    if points:
        x = points
    else:
        x = np.linspace(start, finish, n)

    plt.plot(x, np.array([f(xi) for xi in x]))

def DefinePosition(x,y,dx,dy):
    def F(_x,_y):
        return sum([(_x-x[i]+dx[i])**2+(_y-y[i]+dy[i])**2 for i in range(len(x))])

    def dFx(_x):
        return sum([
            2*(_x-x[i]+dx[i]) for i in range(len(x))
        ])
    def dFy(_y):
        return sum([
            2*(_y-y[i]+dy[i]) for i in range(len(x))
        ])
    eps = 10**(-6)
    g = 0.5
    pos_x = 0
    pos_y = 0

    while F(pos_x, pos_y)>eps:
        new_pos_x = pos_x - g * dFx(pos_x)
        new_pos_y = pos_y - g * dFy(pos_y)

        if F(new_pos_x,new_pos_y) < F(pos_x, pos_y):
            pos_x = new_pos_x
            pos_y = new_pos_y
        else:
            g/=2

        if g<eps:
            break

    return pos_x,pos_y,F(pos_x, pos_y)

if __name__ == '__main__':

    def Task1_1():
        f = lambda x: np.sin(x)

        res = Approximation(f, 2, 2, 0, np.pi)

        Plot(res['polynom'], 0, np.pi, 100)

        res = Approximation(f, 3, 3, 0, np.pi)
        Plot(f, 0, np.pi, 100)
        Plot(res['polynom'], 0, np.pi, 100)
        plt.title('f(x) = sin(x), n = 2;3, m = 2;3')
        plt.show()

        # Графік повністю співпадає
        res = Approximation(f, 30, 30, 0, np.pi)

    def Task1_2():
        f = lambda x: np.e ** x

        res = Approximation(f, 2, 2, 0, 1)

        Plot(res['polynom'], 0, 1, 100)

        Plot(f, 0, 1, 100)

        # Графік повністю співпадає
        res = Approximation(f, 30, 30, 0, 1)

        Plot(res['polynom'], 0, 1, 100)

        plt.title('f(x) = e^x, n = 2; 30, m = 2; 30')
        plt.show()

    def Task2():
        rob_pos_x = np.random.randint(0,3)+np.random.random()
        rob_pos_y = np.random.randint(0,4)+np.random.random()

        n = 5
        errx = np.array([(-1)**np.random.randint(10)*np.random.random()/20 for i in range(n)])
        erry = np.array([(-1)**np.random.randint(10)*np.random.random()/20 for i in range(n)])

        lamp_x = np.array([np.random.randint(0,3)+np.random.random() for i in range(n)])
        lamp_y = np.array([np.random.randint(0,4)+np.random.random() for i in range(n)])

        dx = lamp_x-rob_pos_x+errx
        dy = lamp_y-rob_pos_y+erry

        position = DefinePosition(lamp_x, lamp_y, dx, dy)

        print('Robot position:',rob_pos_x,';',rob_pos_y)
        print('Lamps:',lamp_x,'\n       ',lamp_y)
        print()
        print('Defined position:',position)

    Task2()
