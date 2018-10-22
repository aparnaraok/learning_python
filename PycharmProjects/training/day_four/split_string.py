import re

p = re.compile(r'\W+') #takes out space and comma
lis1  = p.split('This is a test, short and sweet, of split() . ')
print ("List 1>>>", lis1)

#Filters only 3 characters
lis2 = p.split('This is a test, short and sweet, of split() . ', 3)
print ("List 2>>>>>>", lis2)