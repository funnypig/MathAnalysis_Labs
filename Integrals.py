from math import *
import random

output = []

'''
https://jsonformatter.curiousconcept.com/

OUTPUT LINE:

[{"Function": "f(x) = x + cos(x)", "Bounds": "-1.5707963267948966; 1.5707963267948966", "Wolfram calculation": "2", "Calculations": [{"Calculation method": "Rectangle", "Calculation result": 2.0000822490709855, "Info": "n=100"}, {"Calculation method": "Rectangle", "Calculation result": 2.000000008224667, "Info": "n=10000"}, {"Calculation method": "Rectangle", "Calculation result": 2.0000000000822524, "Info": "n=100000"}, {"Calculation method": "Trapezium", "Calculation result": 1.9998355038874436, "Info": "n=100"}, {"Calculation method": "Trapezium", "Calculation result": 1.999999983550658, "Info": "n=10000"}, {"Calculation method": "Trapezium", "Calculation result": 1.9999999998355205, "Info": "n=100000"}, {"Calculation method": "Simpson", "Calculation result": 1.278740628556, "Info": "n=100"}, {"Calculation method": "Simpson", "Calculation result": 1.2950415327087186, "Info": "n=10000"}, {"Calculation method": "Simpson", "Calculation result": 1.295189578364612, "Info": "n=100000"}, {"Calculation method": "MonteCarlo", "Calculation result": 1.597752917570606, "Info": "n=100"}, {"Calculation method": "MonteCarlo", "Calculation result": 1.2950415327087186, "Info": "n=10000"}, {"Calculation method": "MonteCarlo", "Calculation result": 1.295189578364612, "Info": "n=100000"}]}, {"Function": "f(x) = 3^(-x^2)", "Bounds": "0.9; 1", "Wolfram calculation": "0.0371354", "Calculations": [{"Calculation method": "Rectangle", "Calculation result": 0.03713540386611708, "Info": "n=100"}, {"Calculation method": "Rectangle", "Calculation result": 0.037135407189334356, "Info": "n=10000"}, {"Calculation method": "Rectangle", "Calculation result": 0.037135407189663704, "Info": "n=100000"}, {"Calculation method": "Trapezium", "Calculation result": 0.0371354138367656, "Info": "n=100"}, {"Calculation method": "Trapezium", "Calculation result": 0.03713540719033169, "Info": "n=10000"}, {"Calculation method": "Trapezium", "Calculation result": 0.037135407189673494, "Info": "n=100000"}, {"Calculation method": "Simpson", "Calculation result": 0.019597460253376418, "Info": "n=100"}, {"Calculation method": "Simpson", "Calculation result": 0.019591894461048823, "Info": "n=10000"}, {"Calculation method": "Simpson", "Calculation result": 0.01959184385230181, "Info": "n=100000"}, {"Calculation method": "MonteCarlo", "Calculation result": 0.037177511734345775, "Info": "n=100"}, {"Calculation method": "MonteCarlo", "Calculation result": 0.019591894461048823, "Info": "n=10000"}, {"Calculation method": "MonteCarlo", "Calculation result": 0.01959184385230181, "Info": "n=100000"}]}, {"Function": "f(x) = sin(x^10)", "Bounds": "0; 1", "Wolfram calculation": "0.0856934", "Calculations": [{"Calculation method": "Rectangle", "Calculation result": 0.08567083901510453, "Info": "n=100"}, {"Calculation method": "Rectangle", "Calculation result": 0.08569337877786652, "Info": "n=10000"}, {"Calculation method": "Rectangle", "Calculation result": 0.08569338100661324, "Info": "n=100000"}, {"Calculation method": "Trapezium", "Calculation result": 0.0857384398452596, "Info": "n=100"}, {"Calculation method": "Trapezium", "Calculation result": 0.08569338553164578, "Info": "n=10000"}, {"Calculation method": "Trapezium", "Calculation result": 0.08569338107415155, "Info": "n=100000"}, {"Calculation method": "Simpson", "Calculation result": 0.08740347085541374, "Info": "n=100"}, {"Calculation method": "Simpson", "Calculation result": 0.09417506011915844, "Info": "n=10000"}, {"Calculation method": "Simpson", "Calculation result": 0.09418409139708434, "Info": "n=100000"}, {"Calculation method": "MonteCarlo", "Calculation result": 0.12391284935185355, "Info": "n=100"}, {"Calculation method": "MonteCarlo", "Calculation result": 0.09417506011915844, "Info": "n=10000"}, {"Calculation method": "MonteCarlo", "Calculation result": 0.09418409139708434, "Info": "n=100000"}]}, {"Function": "f(x) = x^(-x)", "Bounds": "0; 3", "Wolfram calculation": "1.9788156689153", "Calculations": [{"Calculation method": "Rectangle", "Calculation result": 1.9790011705791075, "Info": "n=100"}, {"Calculation method": "Rectangle", "Calculation result": 1.9788157044521435, "Info": "n=10000"}, {"Calculation method": "Rectangle", "Calculation result": 1.9788156693334282, "Info": "n=100000"}, {"Calculation method": "Trapezium", "Calculation result": 1.9783942507822292, "Info": "n=100"}, {"Calculation method": "Trapezium", "Calculation result": 1.9788155925751552, "Info": "n=10000"}, {"Calculation method": "Trapezium", "Calculation result": 1.978815667955726, "Info": "n=100000"}, {"Calculation method": "Simpson", "Calculation result": 1.549626371236887, "Info": "n=100"}, {"Calculation method": "Simpson", "Calculation result": 1.5463099478298685, "Info": "n=10000"}, {"Calculation method": "Simpson", "Calculation result": 1.54627998008384, "Info": "n=100000"}, {"Calculation method": "MonteCarlo", "Calculation result": 1.8845944689980312, "Info": "n=100"}, {"Calculation method": "MonteCarlo", "Calculation result": 1.5463099478298685, "Info": "n=10000"}, {"Calculation method": "MonteCarlo", "Calculation result": 1.54627998008384, "Info": "n=100000"}]}]

'''

def f1(x):
    return x + cos(x)

def f2(x):
    return 3**(-x**2)

def f3(x):
    return sin(x**10)

def f4(x):
    # own function
    return x**(-x)

def IntegralRectangles(a,b,n,f):
    '''
    Calculate Integral from a to b using rectangle method
    :param a: lower bound
    :param b: upper bound
    :param n: number of rectangles
    :param f: function under the integral
    :return: calculated integral
    '''
    x = [a+(b-a)*i/n for i in range(n+1)]
    return sum([ f( (x[i]+x[i+1])/2 )*(x[i+1]-x[i]) for i in range(n) ])

def IntegralTrapezium(a,b,n,f):
    '''
    Calculate Integral from a to b using trapezium method
    :param a: lower bound
    :param b: upper bound
    :param n: number of trapeziums
    :param f: function under the integral
    :return: calculated integral
    '''
    x = [a+(b-a)*i/n for i in range(n+1)]
    return sum( [ (f(x[i])+f(x[i+1]))/2*(x[i+1]-x[i]) for i in range(n) ] )

def IntegralSimpson(a,b,n,f):
    '''
    Calculate Integral from a to b using Simpson's method
    :param a: lower bound
    :param b: upper bound
    :param n: fragmentation number
    :param f: function under the integral
    :return: calculated integral
    '''
    x = [a+(b-a)*i/n for i in range(n+1)]
    return sum( [1/6*((f(x[i])+4*f( (x[i]+x[i+1]/2 ) ) + f(x[i+1])))*(x[i+1]-x[i])
        for i in range(n)] )

def IntegralMonteCarlo(a, b, n, f):
    '''
    Calculate Integral from a to b using Monte Carlo method
    :param a: lower bound
    :param b: upper bound
    :param n: fragmentation number
    :param f: function under the integral
    :return: calculated integral
    '''
    x = [random.uniform(a,b) for i in range(n+1)]
    return (b-a)/n * sum ( [ f(x[i])  for i in range(n)] )

# test version
outInterface = {"Function":"",
                "Bounds":"",
                "Wolfram calculation":0.00,
                "Calculations":
                    [
                        {
                            "Calculation method":"",
                            "Calculation result":0.00,
                            "Info(optional)":""
                        }
                    ]}

def DoTest(a,b,fx, funcname = "", wolfram = ""):
    return {
    "Function":funcname, "Bounds":"{0}; {1}".format(a,b),
    "Wolfram calculation":wolfram,
                "Calculations":
                    [
                        # RECTANGLE
                        {
                            "Calculation method":"Rectangle",
                            "Calculation result":IntegralRectangles(a,b,100,fx),
                            "Info":"n=100"
                        },
                        {
                            "Calculation method":"Rectangle",
                            "Calculation result":IntegralRectangles(a,b,10000,fx),
                            "Info":"n=10000"
                        },
                        {
                            "Calculation method":"Rectangle",
                            "Calculation result":IntegralRectangles(a,b,100000,fx),
                            "Info":"n=100000"
                        },

                        # Trapezium
                        {
                            "Calculation method":"Trapezium",
                            "Calculation result":IntegralTrapezium(a,b,100,fx),
                            "Info":"n=100"
                        },
                        {
                            "Calculation method":"Trapezium",
                            "Calculation result":IntegralTrapezium(a,b,10000,fx),
                            "Info":"n=10000"
                        },
                        {
                            "Calculation method":"Trapezium",
                            "Calculation result":IntegralTrapezium(a,b,100000,fx),
                            "Info":"n=100000"
                        },

                        # Simpson
                        {
                            "Calculation method":"Simpson",
                            "Calculation result":IntegralSimpson(a,b,100,fx),
                            "Info":"n=100"
                        },
                        {
                            "Calculation method":"Simpson",
                            "Calculation result":IntegralSimpson(a,b,10000,fx),
                            "Info":"n=10000"
                        },
                        {
                            "Calculation method":"Simpson",
                            "Calculation result":IntegralSimpson(a,b,100000,fx),
                            "Info":"n=100000"
                        },

                        # Monte Carlo
                        {
                            "Calculation method":"MonteCarlo",
                            "Calculation result":IntegralMonteCarlo(a, b, 100, fx),
                            "Info":"n=100"
                        },
                        {
                            "Calculation method":"MonteCarlo",
                            "Calculation result":IntegralSimpson(a,b,10000,fx),
                            "Info":"n=10000"
                        },
                        {
                            "Calculation method":"MonteCarlo",
                            "Calculation result":IntegralSimpson(a,b,100000,fx),
                            "Info":"n=100000"
                        }
                    ]
}

a = -pi/2; b = pi/2; fx = f1
output.append(DoTest(a,b,fx,"f(x) = x + cos(x)","2"))

a = 0.9; b = 1; fx = f2
output.append(DoTest(a,b,fx,"f(x) = 3^(-x^2)", "0.0371354"))

a = 0; b = 1; fx = f3
output.append(DoTest(a,b,fx,"f(x) = sin(x^10)","0.0856934"))

a = 0; b = 3; fx = f4
output.append(DoTest(a,b,fx,"f(x) = x^(-x)","1.9788156689153"))

print(str(output).replace("'",'"'))


