import math #ok

n = int(input())
m = int(input())
x = int(input()) #d
y = int(input()) #s

s = min(n, m)
d = max(n, m)

s2 = s - x
d2 = d - y

ans = min(x, y, s2, d2)
print(ans)