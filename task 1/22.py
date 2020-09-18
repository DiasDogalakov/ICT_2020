import math
f = int(input("First: "))
s = int(input("Second: "))
t = int(input("Third: "))
m = (f + s + t) / 2
a = (m*(m-f)*(m-s)*(m-t))**0,5
print("Area of triangle is: " + str(a))
