a = int(input()) #ok
s = input().split()

l = []
cnt = 1
for i in range(0, len(s)):
    l.append(s[i])
l.sort()
for i in range(0, len(l)):
    current = l[0]
for i in range(0, len(l)):
    if(l[i] != current):
        cnt += 1
        current = l[i]
print(cnt)