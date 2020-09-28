x = int(input()) #ok
y = int(input())
x1 = int(input())
y1 = int(input())

X1 = x
Y1 = y + 1

X2 = x
Y2 = y - 1

X3 = x + 1
Y3 = y

X4 = x - 1
Y4 = y

X5 = x - 1
Y5 = y + 1

X6 = x + 1
Y6 = y + 1

X7 = x + 1
Y7 = y - 1

X8 = x - 1
Y8 = y - 1

if x1 == X1 and y1 == Y1:
    print("YES")
elif x1 == X2 and y1 == Y2:
    print("YES")
elif x1 == X3 and y1 == Y3:
    print("YES")
elif x1 == X4 and y1 == Y4:
    print("YES")
elif x1 == X5 and y1 == Y5:
    print("YES")
elif x1 == X6 and y1 == Y6:
    print("YES")
elif x1 == X7 and y1 == Y7:
    print("YES")
elif x1 == X8 and y1 == Y8:
    print("YES")

else:
    print("NO")