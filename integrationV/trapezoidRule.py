import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-x**2)


x = np.linspace(-0.5, 1.5, 100)     # Returns number spaces evenly (interval)
y = f(x)
plt.plot(x, y)

x0 = 0
x1 = 1
y0 = f(x0)
y1 = f(x1)
plt.fill_between([x0, x1], [y0, y1])

plt.xlim([-0.5, 1.5])
plt.ylim([0, 1.5])
plt.show()

A = 0.5*(x1 - x0)*(y1 + y0)
print("Trapezoid area:", A)

