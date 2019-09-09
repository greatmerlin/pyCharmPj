import matplotlib.pyplot as plt
from IPython.display import display
from sympy import *
import numpy as np
from math import *
from scipy.integrate import quad
from scipy.integrate import simps
from numpy import trapz
from mpl_toolkits.mplot3d import Axes3D

# we'll start with a quick explanation of what happens and hints to two functions
print('----------------------------------------------------')
print('')
print('TORUS VOLUME CALCULATOR')
print('')
print('this python sheet is designed to compare different methods to calculate')
print('the volume of a rotated circle body, i.e. torus')
print('')
print('we will use following methods:')
print('')
print('- exact calculation')
print('- iterated trapeze method')
print('- trapeze library method')
print('- iterated simpson method')
print('- simpson library method')
print('- integrated method')
print('')
print('following functions are available:')
print('')
print('newTorus(hole_rad, diam_tube) \t new calculation for specific torus volume')
print('printIterations() \t\t overview of trapeze/simpson iterations')
print('')
print('----------------------------------------------------')

# start
init_printing(use_latex='mathjax', no_global=True)
x, r, R = symbols('x r R')
f, g, h = symbols('f g h', cls=Function)

# ---------------------- change circle attributes here ----------------------

# definition of rotated circle
rotated_circle_start_height = 1  # circle is placed this high above x axis
rotated_circle_diameter = 1  # circle diameter

# ---------------------- change circle attributes above ----------------------

# global variables
rad_max = 0  # translation to max radius of rotation body
rad_hole = 0  # translation to min radius of rotation body (i.e. 'hole')
rad_tube = 0  # radius of torus tube (i.e. 'r')
rad_torus = 0  # radius of torus (i.e. 'R')
result_t = 0  # trapeze value calculated with iterations
result_s = 0  # simpson value calculated with iterations
lib_t = 0  # trapeze value calculated with numpy library
lib_s = 0  # simpson value calculated with scipy library
x_ = 0  # x values for 3d plot
y_ = 0  # y values for 3d plot
z_ = 0  # z values for 3d plot
integrated = 0  # variable will store integrated result
V = 0  # variable for exact volume

lim_a = 0  # x value for starting integral calculations
n_iter = 10  # iteration base value will be 2**n_iter
theta = np.linspace(0, 2 * pi, 100)  # theta value for 3d plot
phi = np.linspace(0, 2 * pi, 100)  # phi value for 3d plot
theta, phi = np.meshgrid(theta, phi)  # theta and phi as mesh grid

# formula for circle scope
expr_a = 'sqrt(r**2-x**2)'
f = lambdify([x, r], sympify(expr_a), "numpy")

# formulas for circle volume
g = lambda x, R, r: x * np.sqrt(r ** 2 - (x - R) ** 2)
h = lambda R, r: 2 * pi ** 2 * R * r ** 2


# helper functions
# source: http://www.imn.htwk-leipzig.de/~lueders/informatik/lehrinhalte/torus.pdf
def volume(a, b):
    """function will return the volume of a torus.
    parameters:
        a: 1/2 area of cut torus 'cap' (equals half circle area of rotated circle)
        b: 1/2 area of cut torus itself"""
    return ((2 * b - (2 * b - 4 * a)) * rad_torus) * pi * 2


# source: https://scipython.com/book/chapter-7-matplotlib/examples/a-torus/
def plot():
    """function will plot 3d graph of torus"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_zlim(-rad_torus, rad_torus)
    ax.plot_surface(x_, y_, z_, rstride=5, cstride=5, color='#FF9321', edgecolors='w')
    ax.view_init(45, 30)
    plt.title('volume will be calculated for displayed torus', y=1.08)
    plt.show()


# source: https://stackoverflow.com/questions/46431826/using-trapezoidal-numerical-integration-in-python
def trapeze(add, n):
    """trapeze approximation formula, iteration will be done n times"""
    a = lim_a
    b = rad_tube
    r = b
    h = (b - a) / n
    sum = ((f(a, r) + add) + (f(b, r)) + add) / 2.
    for i in range(1, n):
        sum = sum + (f((a + (h * i)), r) + add)
    return sum * h


# source: https://stackoverflow.com/questions/16001157/simpsons-rule-in-python
def simpson(add, n):
    """simpson approximation formula, iteration will be done n times"""
    a = lim_a
    b = rad_tube
    r = b
    h = (b - a) / n
    k = 0.0
    x = a + h
    for i in range(1, int(n / 2 + 1)):
        k += 4 * (f(x, r) + add)
        x += 2 * h
    x = a + 2 * h
    for i in range(1, int(n / 2)):
        k += 2 * (f(x, r) + add)
        x += 2 * h
    return (h / 3) * ((f(a, r) + add) + (f(b, r) + add) + k)


def prepareIterations(title, function, iterations):
    """function to display multiple iterations of either the trapeze or simpson formula"""
    print(title + ' calculation:')
    print('iterations', '\tresult', '\t\terror (delta exact volume)')
    for i in range(1, iterations + 1):
        n = 2 ** i
        t1 = function(0, n)
        t2 = function(rad_torus, n)
        t = volume(t1, t2)
        print('%d \t\t%f \t%s' % (n, t, error(t)))
    print('')


def printIterations():
    """function prints multiple iterations of trapeze and simpson formula"""
    prepareIterations('trapeze', trapeze, n_iter)
    prepareIterations('simpson', simpson, n_iter)


def calcResult(function, iterations):
    """function will return the result for either the trapeze or simpson formula
    for specific iterations"""
    t1 = function(0, iterations)
    t2 = function(rad_torus, iterations)
    t = volume(t1, t2)
    return t


def newTorus(hole_rad, diam_tube):
    """function allows to run the calculations for another rotated circle body (=torus).
    if hole_rad or diam_tube are null or smaller, it will be set to 0.000001 to prevent errors.
    parameters are:
        - hole_rad (radius of the torus hole)
        - diam_tube (diameter of the circle to be rotated)"""
    global rotated_circle_start_height
    global rotated_circle_diameter
    if hole_rad <= 0:
        hole_rad = 0.000001
    if diam_tube <= 0:
        diam_tube = 0.000001
    rotated_circle_start_height = hole_rad
    rotated_circle_diameter = diam_tube
    perform()


def calc():
    """function will calculate all needed values for a specific torus"""
    # importing global variables
    global rad_max
    global rad_hole
    global rad_tube
    global rad_torus
    global x_
    global y_
    global z_
    global V
    global result_t
    global result_s
    global lib_t
    global lib_s
    global integrated

    # sets upper and lower radius
    rad_max = rotated_circle_start_height + rotated_circle_diameter
    rad_hole = rotated_circle_start_height

    # sets R and r value of torus
    rad_tube = (rad_max - rad_hole) / 2
    rad_torus = rad_max - rad_tube

    # sets axe values for 3d plot
    x_ = (rad_torus + rad_tube * np.cos(theta)) * np.cos(phi)
    y_ = (rad_torus + rad_tube * np.cos(theta)) * np.sin(phi)
    z_ = rad_tube * np.sin(theta)

    # gets exact volume
    V = h(rad_torus, rad_tube)

    # calculates volume by integral
    integrated, err = quad(g, rad_hole, rad_max, args=(rad_torus, rad_tube))
    integrated *= 4 * pi

    # calculates volume for trapeze and simpson method
    result_t = calcResult(trapeze, 2 ** n_iter)
    result_s = calcResult(simpson, 2 ** n_iter)

    # calculates volume for trapeze and simpson method from libraries
    # setup data points for calculations
    x_num = np.linspace(0, rad_tube, 100)
    y_num_a = f(x_num, rad_tube)
    y_num_b = f(x_num, rad_tube) + rad_torus

    # calculate volume of torus
    lib_t = volume(trapz(y_num_a, x=x_num), trapz(y_num_b, x=x_num))
    lib_s = volume(simps(y_num_a, x=x_num), simps(y_num_b, x=x_num))


def error(x):
    """function will return the delta error.
    the value to be checked will be compared to the known exact value"""
    return str(100 / V * (V - x)) + ' %'


def printOverview():
    """function will display an overview of all calculations"""
    print('----------------------------------------------------')
    print('')
    print('OVERVIEW:')
    print('')
    print('exact volume: \t\t' + str(V))
    print('')
    print('trapeze value: \t\t' + str(result_t) + '\terror: ' + error(result_t))
    print('numpy.trapz: \t\t' + str(lib_t) + '\terror: ' + error(lib_t))
    print('')
    print('simpson value: \t\t' + str(result_s) + '\terror: ' + error(result_s))
    print('scipy.simps: \t\t' + str(lib_s) + '\terror: ' + error(lib_s))
    print('')
    print('integrated value: \t' + str(integrated) + '\terror: ' + error(integrated))
    print('')
    print('----------------------------------------------------')


def perform():
    """calculates new values, plots torus and prints overview"""
    calc()
    plot()
    printOverview()


# executed as this py sheet is started
perform()