k = float(input())
m = k * 760 / 101.325
a = k / 101.325
p = k / 6.89475
print("Pressure(p) per square inch: " + str(round(p, 2)))
print("Pressure(mm) of mercury: " + str(round(m, 2)))
print("Pressure of atmosphere: " + str(round(a, 2)))
