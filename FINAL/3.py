n = int(input()) #ok
a = [int(i) for i in input().split()]
ans = []
for i in range(n-1): 
    if(a[i+1] == 1): ans.append(a[i])
ans.append(a[n-1])
print(len(ans))
for i in ans:
    print(i , end = ' ')