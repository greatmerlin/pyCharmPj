from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, num=11, endpoint=True)
'#can also be written: x = np.r_[0:10:11j] or x = np.linspace(0, 10, 11)'
y = np.cos(-x**2/9.0)

f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')

xnew = np.linspace(0, 10, num=11, endpoint=True)

plt.plot(x, y, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data' 'linear', 'cubic'], loc='best')
plt.show()