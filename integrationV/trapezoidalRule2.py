import math


def trapezoidalRule(f, a, b, n):

    g = 0
    if b > a:
        h = (b-a)/float(n)
    else:
        h = (a-b)/float(n)

    for i in range(0, n):
        k = 0.5 * h * (f(a + i * h) + f(a + (i + 1) * h))
        g = g + k

    return g


print(trapezoidalRule(math.sin, 0, 0.5 * math.pi, 10))
print(trapezoidalRule(abs, -1, 1, 10))
print(trapezoidalRule(lambda x: x**2, 5, 10, 100))
