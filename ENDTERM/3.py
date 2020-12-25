N, X = input().split()
n = int(N)
x = int(X)
ans = 0
for i in range(1, n+1):
    if(x % i == 0 and x / i <= n):
        ans += 1
print(ans)