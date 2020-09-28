import math
n = int(input())
m = int(input())
k = int(input())

check = 1

if(check == 1):
    c = min(n, m)
    cnt = c #ширина
    while cnt < k:
        cnt += c
    if cnt == k:
        check = 0
        print("YES")

elif(check == 1):
    c = max(n, m)
    cnt == c
    while cnt < k:
        cnt += c
    if cnt == k:
        check = 0
        print("YES")

elif(check == 1):
    print("NO")