import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**2

###################################################################
# comment below to hide the diagram using 10 * N = 1000
###################################################################


a = 5
b = 10
N = 1000
n = 10  # Use n * N + 1 points to plot the function smoothly

x = np.linspace(a, b, N + 1)
y = f(x)

X = np.linspace(a, b, n * N + 1)
Y = f(X)

x = np.linspace(a, b, N + 1)
y = f(x)

X = np.linspace(a, b, n * N + 1)
Y = f(X)

plt.plot(X, Y)

for i in range(N):
    xs = [x[i], x[i], x[i + 1], x[i + 1]]
    ys = [0, f(x[i]), f(x[i + 1]), 0]
    plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)

plt.title('Trapezoid Rule, N = {}'.format(N))
plt.show()

###################################################################
# now print the results using N = 10000
###################################################################


def simpson(a, b, n):
    dx = (b-a)/n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    result = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    return result


S = simpson(5, 10, 10000)


print("Simsons Rule:  ", S)

# compare the simsons rule to the approximation value of https://www.integral-calculator.com/

I = 291.6666666666667
print("Real Value:    ", I)

# print the error

print("Simsons Rule Error:", np.abs(I - S))


exit()

