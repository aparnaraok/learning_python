tup1 = (12,3.12,'hello',[1,2],-14,1.21,10,'world')
print ("Tuple is : : ", tup1)

li1 = [12,3.12,'hello',(1,2),-14,1.21,10,'world']
print ("List is : : ", li1)

'''
li1[3] = 21
print (li1)

tup1[3][0] = 5
print (tup1)

li1.insert(2,80)
print ("After inserting >>>", li1)

li1.append(100)
print ("after appending.>>>>", li1)

li1.extend([100,200])
print ("li1 is ",id(li1), li1)
li1 = li1+[100, 200]
print (id(li1))

print (li1)
'''
li4 = [1,2,3,4,5,10,19,10,19]
print (li4)
print (li4.index(10,5))

print (li4.count(19))
li4.remove(10)
print (li4) ##Removes the first occurence of 10

'''Same address print'''
print (id(li4))
li4.extend([100,200])
#li4 = li4 + [100, 200]
print (id(li4))

'''Different address print'''
print (id(li4))
#li4.extend([100,200])
li4 = li4 + [100, 200]
print (id(li4))

print (li4)
li4.pop(7)
print ("after popping>>>", li4)

li4.remove(3)
print ("After removing>>>>", li4)

li4.pop()
print (li4)

del[li4[1]]
print (li4)

li5 = [5,2,6,8]
li5.reverse()
print ("After reversing>>>", li5)

print ("Original list>>>>>", li5)
li5.sort()
print ("After Sorting>>>>", li5)


tux = 9
tuy = 9,
#print (tux[0])
print (tuy)
print (tuy[0])