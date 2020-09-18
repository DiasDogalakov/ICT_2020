v = float(input("Water(ml): "))
t = float(input("Temp(Cel) increase: "))
p = float(input("Electricity: "))
JtoK = 2.777e-7
h_cap = 4.186
e = v * t * h_cap
k = e * JtoK
ans = k * p
print("Energy: " + str(round(e, 2)))
print("Joules, price: " + str(round(ans, 2)))
