import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2


a = 5
b = 10
N = 1000
n = 10  # Use n * N + 1 points to plot the function smoothly

x = np.linspace(a, b, N + 1)
y = f(x)

X = np.linspace(a, b, n * N + 1)
Y = f(X)

###################################################################
# comment below to hide the diagram using 10 * N = 1000
###################################################################

plt.plot(X, Y)

for i in range(N):
    xs = [x[i], x[i], x[i + 1], x[i + 1]]
    ys = [0, f(x[i]), f(x[i + 1]), 0]
    plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)

plt.title('Trapezoid Rule, N = {}'.format(N))
plt.show()


###################################################################
# now compute and print the sum of areas of the trapezoids:
###################################################################


y = f(x)
y_right = y[1:]  # Right endpoints
y_left = y[:-1]  # Left endpoints
dx = (b - a)/N
T = (dx/2) * np.sum(y_right + y_left)
print("Trapezoid Rule:", T)

# compare the trapezoid rule to the approximation value of https://www.integral-calculator.com/

I = 291.6666666666667
print("Real Value:    ", I)

# print the error

print("Trapezoid Rule Error:", np.abs(I - T))

exit()
