li1 = [2,4,5,6,11,3,7,11,3,5,5]
'''
for ele in li1:
    if li1.count(ele) > 1:
        print ("The index of the repeated element ", ele , "is", li1.index(ele))

'''

'''Get the elements that are repeated more than once and print its indices'''
for i in range(0, len(li1)):
    if li1.count(li1[i]) > 1:
        print ("The index of the ele ", li1[i] , "is", i)

for i in range(0, len(li1)):
    if li1[i] == 11:
        print (i)


'''Remove the duplicate elements from the list'''
new_list = []
for ele in li1:
    if not ele in new_list:
        new_list.append(ele)
print ("New list>>>>>", new_list)

print (set(li1))

set1 = set(li1)
new_list = []
list2 = list(set1)
'''
for i in set:

    if i not in new_list:
        new_list.append(i)
        set1.remove(i)
    if not set:
        break
print ("NEW LISTTTT>>>>>>>", new_list)
'''

user = {'name':'sandeep', 'pass':'somepass','uid':5012, 'ext' : 9012}
'''
val = input("Enter the value......")

for (k, v) in user.items():
    if v == val or v == int(val):
        print ("Key found for the value : ", val, "is ", k)
        break
    else:
        print ("No key value pair found for the value : ",val)
'''
new_list =[]
li2 = [1,2,3,4,3,2,4,5]
set2 = set(li2)
li3 = list(set2)
for i in li2:
    if i in li3:
        new_list.append(i)
        li3.remove(i)
    if li3==[]:
        break
print(new_list)




