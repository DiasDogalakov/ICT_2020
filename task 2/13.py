check = True #ok
ans = 0
while(check):
    num = int(input())
    if(num == 0):
        check = False
    else:
        ans += num
print(ans)