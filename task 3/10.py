s = str(input())
ss = s.lower()

first = s[0] #первая буква
second = s[1:] # вторая часть слова

fUp = first.upper()
sUp = second.upper()
fL = first.lower()
sL = second.lower()

if(s == ss):
    print(s)
elif(first == fL and second == sUp): #cAPS
    print(ss[0].upper(),end='' + ss[1:])
elif(first == fUp and second == sUp):
    print(s.lower())
else:
    print(s)
