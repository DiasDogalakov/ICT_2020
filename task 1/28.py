t = float(input("Temp(C): "))
s = float(input("Speed(km/h): "))
wci = 13.12 + (0.6215*t) + (-11.37 * s**(0.16)) + (0.3965 * t * s**0.16)
print(str(round(wci, 1)))
