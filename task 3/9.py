n = int(input())
s = input()
cntA = 0
cntD = 0
for i in range(0, len(s)):
    if(s[i] == "A"):
        cntA += 1
    elif(s[i] == "D"):
        cntD += 1
if(cntA > cntD):
    print("Anton")
elif(cntA < cntD):
    print("Danik")
else:
    print("Friendship")
