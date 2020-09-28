a = int(input()) #ok

f1 = 1
f2 = 1
b = 3
check = 1
summa = 0
while(a > summa):
    if check == 1:
        summa = f1 + f2
        f1 = f2
        f2 = summa
        if summa == a:
            print(b)
            check = 0
        else:
            b += 1
if check == 1:
    print(-1)