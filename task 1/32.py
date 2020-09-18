f = int(input())
s = int(input())
t = int(input())

maxi = max(f, s, t)
mini = min(f, s, t)
print(str(maxi) + str(f + s + t - maxi - mini) + maxi)
