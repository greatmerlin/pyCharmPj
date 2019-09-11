import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.r_[0:10:11j]
y = np.sin(x)

splineRep = interpolate.splrep(x, y, s=0)

xnew = np.r_[0:10:100j]
ynew = interpolate.splev(xnew, splineRep, der=0)

plt.figure()

plt.plot(x, y, 'ro')
plt.plot(xnew, ynew, 'b--')

plt.legend(['data points', 'Cubic Spline', 'True'])


plt.title('Cubic-spline interpolation')
plt.show()

# uncomment below for: 1-Derivative estimation from spline

# yder = interpolate.splev(xnew, splineRep, der=1)
# plt.figure()
# plt.plot(xnew, yder, 'ro', xnew, np.cos(xnew), '-')
# plt.legend(['Cubic Spline', 'True'])
#
# plt.title('1-Derivative estimation from spline')
# plt.show()

# uncomment below for: 2-Derivative estimation from spline

# yder = interpolate.splev(xnew, splineRep, der=2)
# plt.figure()
# plt.plot(xnew, yder, 'r--', xnew, np.cos(xnew), '-')
# plt.legend(['Cubic Spline', 'True'])
#
# plt.title('2-Derivative estimation from spline')
# plt.show()
