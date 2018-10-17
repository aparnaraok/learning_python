li = [1,2,19,4,56,7,3,19,19,19,34,78,19,45,62,19,89,19,19,19,1,90,19,68]

li1 = len(li)
i = 0
while i<li1:
    if li[i] == 19:
        li.remove(li[i])
    i += 1
print (li)

ind_list = []
for index, ele in enumerate(li):
    if ele == 19:
        ind_list.append(index)
ind_list.reverse()
print (ind_list)

for ind in ind_list:
    li.pop(ind)

print (li)

while 19 in li:
    li.remove(19)
print ("li>>>>", li)


