s = input() #ok
l = []
check = True
checkForPrint = False
for i in range(0, len(s)):
    if(int(ord(s[0])) >= 65 and int(ord(s[0]) <= 90)):
        checkForPrint = True
        check = False

if(checkForPrint):
    print(s)

if(check):
    for i in range(0, len(s)):
        if(i == 0):
            l.append(chr(int(ord(s[i]) - 32)))
        else:
            l.append(s[i])
print(*l)