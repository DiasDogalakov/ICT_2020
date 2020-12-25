a = int(input())
cnt = 0
ans = []
while(cnt < a):
    cnt+=1
    s = str(input())
    nachalo = -1
    konec = -1
    one = 0
    for i in range(0, len(s)):
        if nachalo == -1:
            if s[i] == '1':
                nachalo = i
                one += 1
        elif s[i] == '1':
            konec = i
            one += 1
    if one <= 1:
        ans.append('0')
    else:
        ans.append(konec - nachalo - one + 1)
for i in range(0, len(ans)):
    print(ans[i])