s1 = input() #ok
s = str(s1.lower())
l = []
for i in range(0, len(s)):
    if(s[i] != 'a' and s[i] != 'o' and s[i] != 'y' and s[i] != 'e' and s[i] != 'u' and s[i] != 'i'):
        l.append('.')
        l.append(s[i])
print(*l)
