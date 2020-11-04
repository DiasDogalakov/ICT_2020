s = input()
currentCNT = 0
check = 0
for i in range(0, len(s)):
    if(s[i] == '1'):
        currentCNT += 1
        if(currentCNT > 6):
            check += 1
    else:
        currentCNT = 0

cnt = 0
ch = 0
for i in range(0, len(s)):
    if(s[i] == '0'):
        cnt += 1
        if(cnt > 6):
            ch += 1
    else:
        cnt = 0

if(check != 0 or ch != 0):
    print("YES")
else:
    print("NO")
