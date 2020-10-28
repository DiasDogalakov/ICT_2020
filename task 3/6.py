s = input() #ok
cntUP = 0
cntLOW = 0
for i in range(0, len(s)):
    if(int(ord(s[i])) >= 65 and int(ord(s[i]) <= 90)):
        cntUP+=1
    elif(int(ord(s[i])) >= 97 and int(ord(s[i])) <= 122):
        cntLOW+=1
if(cntUP > cntLOW):
    print(s.upper())
elif(cntUP < cntLOW):
    print(s.lower())
else:
    print(s.lower())