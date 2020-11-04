a = int(input())
s = input()
currentCNT = 0
ans = 0
for i in range(0, len(s)):
    if(s[i] == "x"):
        currentCNT += 1
        if(currentCNT > 2):
            ans += 1
    else:
        currentCNT = 0
print(ans)
