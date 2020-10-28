s = input() #ok
l = []
l2 = []
for i in range(0, len(s)):
    if(s[i] != '+'):
        l.append(s[i])
l.sort()
for i in range(0, len(l)):
    if(len(l) == 1):
        l2.append(l[i])
    else:
        if(l[i] == l[0]):
            l2.append(l[i])
            l2.append("+")
        elif(i == len(l) - 1):
            l2.append(l[i])
        else:
            l2.append(l[i])
            l2.append("+")
print(*l2)