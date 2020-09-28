a = int(input()) #ok
s = input().split()

l = []
l2 = []
first = 0
last = 0
for i in range(0, len(s)):
    l.append(s[i])
for i in range(0, len(l)):
    length = len(l)
    first = l[0]
    last = l[length - 1]
for i in range(0, len(l)):
    if l[i] == first:
        l2.append(last)
    elif l[i] == last:
        l2.append(first)
    else:
        l2.append(l[i])
print(*l2, end = " ")