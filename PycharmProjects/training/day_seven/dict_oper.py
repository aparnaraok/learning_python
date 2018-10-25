d1 = {'a' : 5, 't' : 3, 'c' : 4, 'e' : 7}
d2 = {'a' : 3, 'l' : 9, 'e' : 1, 'd' : 6}

#union
#intersection
#symmetric diff (uncommon keys tcld)
#subtraction (a e ...a - a(intersection)b)
#issubset
#A is a subset of B if all keys of A are in B and more also ok.
#B is a subset of A if all keys of B are in A and more also ok.

k1_list = []
k2_list = []
out_dict = {}
union_dict = {}

for k1 in d1.keys():
    k1_list.append(k1)
    k1_set = set(k1_list)
for k2 in d2.keys():
    k2_list.append(k2)
    k2_set = set(k2_list)
print ("k1 set>>>", k1_set)
print ("k2 set >>>", k2_set)

#union
u = k1_set.union(k2_set)
tempDict = {}
for eachI in u:
    t = []
    if not d1.get(eachI) is None:
        t.append(d1.get(eachI))
    if not d2.get(eachI) is None:
        t.append(d2.get(eachI))
    tempDict[eachI] = t
print ("temp dict >>>", tempDict)

print ("Union >>>", u)
#intersection
i = k1_set.intersection(k2_set)
print ("Intersection >>>", i)
#subtractor
su = k1_set.difference(k2_set)
print ("Difference >>>", su)

temp_sub_dict = {}
for each_item in su:
    d_list = []
    if not d1.get(each_item) is None:
        d_list.append(d1.get(each_item))
    if not d2.get(each_item) is None:
        d_list.append(d2.get(each_item))
    temp_sub_dict[each_item] = d_list
print ("Subtractor dict >>>", temp_sub_dict)

sy = k1_set.symmetric_difference(k2_set)
print ("Symmetric diff>>>", sy)

temp_sym_dict = {}
for each_item in sy:
    sy_list = []
    if not d1.get(each_item) is None:
        sy_list.append(d1.get(each_item))
    if not d2.get(each_item) is None:
        sy_list.append(d2.get(each_item))
    temp_sym_dict[each_item] = sy_list
print (" Symmetric Subtractor dict >>>", temp_sym_dict)


sub = k1_set.issubset(k2_set)
print ("Subset is >>>", sub)
Aliter way of getting keys
# key1 = set(d1)
# print ("Key 1 >>>", key1)

for k1, v1 in d1.items():
    for k2, v2 in d2.items():
        if k1 == k2:
          union_dict[k1] = [v1, v2]

print ("Union dict >>>",   union_dict)

