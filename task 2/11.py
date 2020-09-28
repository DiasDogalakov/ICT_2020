a = int(input()) #ok

for i in range (2, a):
    if a % i == 0:
        ans = i
        break
print(ans)
    