li1 = [1,2,3,2,3,-1,-4,10]
li2 = [2,1,3,2,5,-2,-4,-10]

s1 = set(li1)
s2 = set(li2)

print ("s1 is ", s1)
print ("s2 is ", s2)

print ("Union is :", s1.union(s2))
print ("Intersection is : ", s1.intersection(s2))
print ("Subset is :", s1.issubset(s2))
print ("Intersection update :", s1.intersection_update(s2))

