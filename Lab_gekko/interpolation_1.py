import numpy as np
from scipy import interpolate
import pylab as py

x = np.r_[0:10:11j]
y = np.exp(-x/8)*x

f = interpolate.interp1d(x, y, kind='cubic')

xnew = np.r_[0:10:100j]

py.figure(1)
py.clf()
py.plot(x, y, 'ro', label='data')
py.plot(xnew, f(xnew), 'b-', label='cubic spline')
py.legend(loc='lower right')

py.show()
