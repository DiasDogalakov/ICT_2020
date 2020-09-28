check = True #ok
cnt = 0
maxi = 0
l = []
while(check):
    num = int(input())
    if(num == 0):
        check = False
    else:
        l.append(num)
l.sort()
for i in range(0, len(l)):
    length = len(l)
    maxi = l[length-1]
for i in range(0, len(l)):
    if(l[i] == maxi):
        cnt += 1
print(cnt)