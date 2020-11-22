def chech_to_anagram(s1, s2): #ok 8
    if(sorted(s1) == sorted(s2)):
        print("YES")
    else:
        print("NO")

s1 = str(input())
s2 = str(input())
chech_to_anagram(s1, s2)