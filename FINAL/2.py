n = int(input()) #ok
a = [int(i) for i in input().split()]
maxi = a[0]
mini = a[0]
for i in a:
    if(maxi < i): maxi = i
    if(mini > i): mini = i
print(maxi - mini + 1 - n)