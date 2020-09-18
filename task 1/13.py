c = int(input())
print(str(c // 200) + "t")
c = c % 200
print(str(c // 100) + "l")
c = c % 100
print(str(c // 25) + "q")
c = c % 25
print(str(c // 10) + "d")
c = c % 10
print(str(c // 5) + "n")
c = c % 5
print(str(c // 1) + "p")
