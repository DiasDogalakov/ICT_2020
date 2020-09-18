d = int(input())
h = int(input())
m = int(input())
s = int(input())
spd = 86400
spm = 60
sph = 3600
ans = d * spd
ans = ans + h*sph
ans = ans + m*spm
ans = ans + s
print(ans)
