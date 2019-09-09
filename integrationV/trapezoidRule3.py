import numpy as np


def trapz(f, a, b, N=50):

    '''Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/2) \sum_{k=1}^N (f(x_k) + f(x_{k-1}))
    where x_k = a + k*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal length.

    Examples
    --------
    -> trapz(np.sin,a=0,b=np.pi/2,N=1000)
    0.99999979438323316
    '''


    x = np.linspace(a, b, N + 1)
    y = f(x)
    y_right = y[1:]     # Right endpoints
    y_left = y[:-1]     # Left endpoints
    dx = (b - a)/N
    T = (dx/2) * np.sum(y_right + y_left)
    return T

print(trapz(np.sin,0,np.pi/2,1000))
print(trapz(lambda x : 3*x**2,0,1,10000))
print(trapz(lambda x : x,0,1,1))

