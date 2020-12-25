n = int(input()) #ok
s = input()
cnt_sea = 0
cnt_fan = 0
for i in range(n):
    if(i < n - 1 and s[i] == 'F' and s[i+1] == 'S'): cnt_sea+=1
    if(i < n - 1 and s[i] == 'S' and s[i+1] == 'F'): cnt_fan+=1
if(cnt_fan>cnt_sea): print("YES")
else: print("NO")