import math
T1 = float(input())
G1 = float(input())
T2 = float(input())
G2 = float(input())
print(str(6371.01 * math.acos(math.sin(T1)*math.sin(T2)+math.cos(T1)*math.cos(T2)*math.cos(G1-G2))))
