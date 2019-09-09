from scipy.integrate import quad
# or: import scipy.integrate.quad as q


def f(x):                     # define the function
    return 3.0 * x**2 + 1


i = quad(f, 0, 2)              # integrate it with this command
print(i)                       # two values, the first one is the integral and the second one the estimate of the air


# to print them separately:
# i,  err = quad(f, 0, 2)
# print(i)
# print(err)

# or without the error
# i = quad(f, 0, 2)
# print(i[0])  -> just to get the integration, the integral



