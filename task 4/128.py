def reverseLp(dic, b): #ok 1
    keys = []
    for i,j in dic.items():
        if j == b:
            keys.append(i)
    return keys


dic = {'Almaty': 1, 'Astana': 2, 'Semey': 3}
print(reverseLp(dic, 1))
print(reverseLp(dic, 2))
print(reverseLp(dic, 3))
