p = float(input("Pressure(p): "))
v = float(input("Volume(l): "))
t = float(input("Temp(C): "))
m = (0.001 * v * p) / (8.314 * (t + 273.15))
print("Moles: " + str(round(m, 1)))
