n = int(input())
ans = 0
a = (n//2)
for i in range(1, a):
    if ((n-i)%i == 0):
        ans+=1
print(ans+1)