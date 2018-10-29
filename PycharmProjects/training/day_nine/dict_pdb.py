user = {'name':'sandeep', 'pass':'somepass','uid':5012, 'ext' : 9012}
print (user['uid'])

user['cell'] = 9008876548

print (user)

#print (dir(user))

print (user.keys())
print (user.values())

print (user.items())

print (user.pop('pass'))
print ("After popping....", user)
import pdb
print (user.setdefault.__doc__)
pdb.set_trace()
user.setdefault('a',100)
print (user)

k1 = input("Enter the Key")
if k1 in user:
    print (k1 , "has value ", user[k1])
else:
    print ("No such key")


user.update({4:'four'})
print (user)


for k in user.keys():
    print ("KEY IS >>>>", k , "=>", user[k])

for (k,v) in user.items():
    print (k , "===>>>", v)


import copy
dic2 = copy.deepcopy(user)
print ("After copying>>>>>", dic2)

# 5012
# {'name': 'sandeep', 'cell': 9008876548, 'uid': 5012, 'ext': 9012, 'pass': 'somepass'}
# dict_keys(['name', 'cell', 'uid', 'ext', 'pass'])
# dict_values(['sandeep', 9008876548, 5012, 9012, 'somepass'])
# dict_items([('name', 'sandeep'), ('cell', 9008876548), ('uid', 5012), ('ext', 9012), ('pass', 'somepass')])
# somepass
# After popping.... {'name': 'sandeep', 'cell': 9008876548, 'uid': 5012, 'ext': 9012}
# D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
# > /home/cisco/PycharmProjects/training/day_one/dict.py(20)<module>()
# -> user.setdefault('a',100)
# (Pdb) 200
# 200

#(Pdb) c
#{'name': 'sandeep', 'a': 100, 'uid': 5012, 'ext': 9012, 'cell': 9008876548}