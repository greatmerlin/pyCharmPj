def f(x):
    return x**2


a = float(input("a: "))     # a = 2.0
b = float(input("b: "))     # b = 3.0

n = 100000

breite_a = a/n
breite_b = b/n


integral_a = 0
integral_b = 0


for i in range(0, n+1):                         # n+1 da für range 0,9 , es geht von 0 bis 9
    integral_a += breite_a * f(i * breite_a)


for i in range(0, n+1):
    integral_b += breite_b * f(i * breite_b)

print(integral_b - integral_a)
