t = int(input()) #ok
l = []
for i in range(t):
    n, m = map(int, input().split())
    if(n % m == 0): l.append("YES")
    else: l.append("NO")
for i in range(0, len(l)):
    print(l[i])