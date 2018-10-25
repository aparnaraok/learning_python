li = [[1,2], [3, [5,6]], 7]
dic1 = {}
dic2 = {}

lis1 = []
l12 = []

for i1, v1 in enumerate(li):
    print (str(i1) + ": " + str(v1))
    dic1[i1] = v1
#print (dic1)
    if type(v1) is list:
        for i11, v11 in enumerate(v1):
            dic2[i11] = v11
            #lis1.append((i1, v1, i11, v11))

            if type(v11) is list:
                for i12, v12 in enumerate(v11):

                    #lis1.append((i1, v1, i11, v11, i12, v12))
                    l12.append((i1, i11, i12))
                    dic2[v12] = l12
            else:
                if not((i1, v1, i11, v11)) in lis1:
                    lis1.append((i1, v1, i11, v11))

    else:
        lis1.append((i1, v1))
print (lis1)

print (dic2)