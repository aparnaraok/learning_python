#print the transpose
li = [[1,2], [3,4], [5,6]]

new_list = []
for i in range(0, len(li[0])):
    print ("i is >>", i)
    trans_list =  []
    for j in range(0, len(li)):
        trans_list.append(li[j][i])
    new_list.append(trans_list)
print ("Transpose >>>>", new_list)