year = int(input())
check = True

a = 0
b = 0
c = 0
d = 0   
while(check):
    year += 1
    a = year/1000
    b = year/100%10
    c = year/10%10
    d = year%10
    if(a!=b and a!=c and a!=d and b!=c and b!=d and c!=d):
        check = False
print(year)