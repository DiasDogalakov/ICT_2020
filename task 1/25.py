t = int(input())
d = t//(86400)
t = t % (86400)
h = t // 3600
t = t % 3600
m = t // 60
t = t % 60
print(d + " " + h + " " + m + " " + t)
