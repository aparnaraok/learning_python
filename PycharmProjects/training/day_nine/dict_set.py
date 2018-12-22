keys = ['a', 'aa', 'aaa']
d1 = dict((k, len(k)) for k in keys)
d2 = dict((k, len(k)) for k in reversed(keys))
print ("d1 : ", d1)
print ("d2 : ", d2)
print ("d1 == d2 : ", d1 == d2)

s1 = set(keys)
s2 = set(reversed(keys))

print (" ")
print("s1 : ", s1)
print ("s2 : ", s2)
print ("s1 == s2:", s1 == s2)


# d1: {'a': 1, 'aa': 2, 'aaa': 3}
# d2: {'a': 1, 'aa': 2, 'aaa': 3}
# d1 == d2: True
#
# s1: {'a', 'aa', 'aaa'}
# s2: {'a', 'aa', 'aaa'}
# s1 == s2: True
#
# Process
# finished
# with exit code 0