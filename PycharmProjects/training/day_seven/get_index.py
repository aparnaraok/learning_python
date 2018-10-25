li = [[1,2], [3, [5,6]], 7]
dic1 = {}
dic2 = {}

lis1 = []

for i1, v1 in enumerate(li):
    print (str(i1) + ": " + str(v1))
    dic1[i1] = v1
#print (dic1)
    if type(v1) is list:
        for i11, v11 in enumerate(v1):
            dic2[i11] = v11
            lis1.append((i1, v1, i11, v11))


    else:
        lis1.append((i1, v1))
print (lis1)