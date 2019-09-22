from mpmath import *

mp.dps = 30
mp.pretty = True

y = findroot(sin, 3)

print(y)

