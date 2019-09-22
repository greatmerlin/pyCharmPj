from sympy import *
from random import random

# Newton's Method with sympy

x = Symbol('x')
# f is the real valued function
f = (x**5.0) - (3.0*(x**2.0)) - 17.0
# g = df/dx = f'(x)
g = diff(f, x)

i = 0
z = random()
MAX_ITER = 100

# that is the Newton's Method itself
while(abs(f.subs(x, z)) > 1E-8 or i < MAX_ITER):
    i = i + 1
    z = z - (f.subs(x, z) /g.subs(x, z))

# we put the result onto screen
print("Estimated Root = " + str(z))
