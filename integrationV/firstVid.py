import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import*


def f(x):                           # we define the function
    return x**2                     #3.0*x*x + 1.0


I, err = quad(f, 0, 1)              # we call the Integral and the error, and then the quad method(function and bounds)

print("I     = ", I)
print("error = ", err)              # we g et a really small error value
