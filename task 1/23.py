from math import pi
import math
n = int(input())
s = int(input())
a = n * (s**2) / (4 * math.tan(pi/n))
print(a)
