a = int(input()) #ok
s = input()

s = s.lower()

l = []
uniqList = []

for i in range(0, len(s)):
    l.append(s[i])
l.sort()
for i in l:
    if(i not in uniqList):
        uniqList.append(i)
if(len(uniqList) == 26):
    print("YES")
else:
    print("NO")