n = int(input())
k = int(input())

l = []
for i in range(1, n + 1):
    l.append(i)
cnt = 0
while(cnt <= k):
    a = 0
    b = 0
    cnt += 1
    s = input().split()
    for i in range(0, len(s)):
        a = int(s[i])
    for i in range(0, len(s)):
        if(s[i] != a):
            b = int(s[i])
    for i in range(0, len(l)):
        if (l[i] >= a and l[i] <= b):
            l[i] = "."
print(*l, end = " ")
