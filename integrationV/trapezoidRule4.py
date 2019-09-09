import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2


x = np.linspace(4.5, 10.5, 100)         # Returns number spaces evenly (interval)
y = f(x)
plt.plot(x, y)

a = 5
b = 10
y0 = f(a)
y1 = f(b)
plt.fill_between([a, b], [y0, y1])

plt.xlim([4, 11])
plt.ylim([0, 120])
plt.show()

A = 0.5*(b - a)*(f(b) + f(a))
print("Trapezoid area:", A)

