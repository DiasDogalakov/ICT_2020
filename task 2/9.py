a1 = int(input()) #ok
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

volume_1 = a1 * b1 * c1
volume_2 = a2 * b2 * c2

if(volume_1 == volume_2):
    print("Boxes are equal")
elif(volume_1 > volume_2):
    print("The first box is larger than the second one")
elif(volume_1 < volume_2):
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")