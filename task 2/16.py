check = True #ok
ans = 0
l = []
while(check):
    num = int(input())
    if(num == 0):
        check = False
    else:
        l.append(num)
for i in range(0, len(l)):
    length = len(l)
    if(l[i] != l[0] and l[i] != l[length - 1]):
        if(l[i] > l[i-1] and l[i] > l[i+1]):
            ans += 1
print(ans)