import sympy as sp

x = sp.Symbol('x')
e = sp.integrate(3.0*x**2 + 1, x)


print(e)
