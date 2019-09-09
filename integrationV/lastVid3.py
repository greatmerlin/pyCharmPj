def f(x):
    return x**2


def trapezoidal(a, b, n):
    widthOfOneRectangle = float(b-a)/n
    result = (1/2) * f(a) + (1/2) * f(b)                # almost the same with: 0
    for i in range(1, n + 1):
        result += f(a + i * widthOfOneRectangle)
    result *= widthOfOneRectangle
    return result


print(trapezoidal(5, 10, 1000000))


# a = starting point on X-Axis
# b = ending point on X-Axis
# n = number of rectangles
# area of a trapezoid = 1/2 * (b-a) * (f(a) + f(b))
