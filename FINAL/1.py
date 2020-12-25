n = int(input()) #ok
k = n
while(True):
    res = n
    for i in range(k):
        res-=((k-i) * (i+1))
    if(res >=0): break
    k-=1
print(k)
