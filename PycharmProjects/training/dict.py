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

print (user.setdefault.__doc__)

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
