lis = [[1,2], [2, [5,6]], 3]

lis_1 = []
lis_2 = []
lis_3 = []

for ele in lis:
    if type(ele) is not list:
        lis_1.append(ele)
    else:
        for ele1 in ele:
            if type(ele1) is not list:
                lis_2.append(ele1)
            else:
                for ele2 in ele1:
                    if type(ele2) is not list:
                        lis_3.append(ele2)

print (lis_1)
print (lis_2)
print (lis_3)

#final_list = []
final_list = lis_1 + lis_2 + lis_3
print ("Final list >>>", final_list)