a = int(input())
s = input().split()
cnt = 0
s.sort()
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        cnt += 1
        s[i + 1] = 10000000
print(cnt)