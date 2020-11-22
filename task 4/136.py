def anagram(s1, s2): #ok 9
    if(sorted(s1)== sorted(s2)):
        print("YES")
    else:
        print("NO")
s1 = input()
s11 = set()
s2 = input()
s22 = set()
for i in s1:
    if i != ' ' and i != '!' and i != ',' and i != '.' and i != '?':
        s11.add(i)
for i in s1:
    if i  != ' ' and i != '!' and i != ',' and i != '.' and i != '?':
        s22.add(i)
anagram(s11, s22)
