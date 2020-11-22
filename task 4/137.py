s = input() #ok 10
cnt = 0
scores = {1:['A','E','I','L','N','O','R','S','T','U'],
       2:['D','G'],
       3:['B','C','M','P'],
       4:['F','H','V','W','Y'],
       5:['K'],
       8:['J','X'],
       10:['Q','Z']}
for i in s:
    for j,k in scores.items():
        for l in k:
            if l == i:
                cnt += j
print(cnt)