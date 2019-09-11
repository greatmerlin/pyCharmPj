import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

xm = np.array([0, 1, 2, 3, 4, 5])
ym = np.array([0.1, 0.2, 0.3, 0.5, 1.0, 0.9])

m = GEKKO()

m.x = m.Param(value=np.linspace(-1, 6))
m.y = m.Var()

m.cspline(m.x, m.y, xm, ym)

m.options.IMODE = 2
m.solve(disp=False)

plt.plot(xm, ym, 'bo', label='data points')
plt.plot(m.x, m.y, 'r--', label='cubic spline')
plt.legend(loc='lower right')

plt.show()
