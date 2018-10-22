'''Word match'''
import re
pat_1 = re.compile("san")
#name = input("Enter your name ")
name = "santhosh"
if pat_1.search(name):
    print ("Name matched")
else:
    print ("Name not matched")

'''First char match'''
import re
pat_1 = re.compile("^san")
#name = input("Enter your name ")
name = "sanjana"
if pat_1.search(name):
    print ("Name matched")
else:
    print ("Name not matched")

'''Last char match'''
import re
pat_1 = re.compile("san$")
name = "sujfdasihsan"
#name = input("Enter your name ")
if pat_1.search(name):
    print ("Name matched")
else:
    print ("Name not matched")

'''Exact match'''
import re
pat_1 = re.compile("^san$")
name = "san"
#name = input("Enter your name ")
if pat_1.search(name):
    print ("Name matched")
else:
    print ("Name not matched")

'''To match exactly a number enclose pattern with ^ and $'''
import re
pat_1 = re.compile("^[0-9]+$")
cell = '9797097070'
#cell = input("Enter your cell number ")
if pat_1.search(cell):
    print ("Num matched")
else:
    print ("Num not matched")

'''Only searches for a num'''
import re
pat_1 = re.compile("[0-9]")
cell = "gfsgugfu7"
#cell = input("Enter your cell number ")
if pat_1.search(cell):
    print ("Num matched")
else:
    print ("Num not matched")


'''dot match'''
pat1 = re.compile('[0-9]+')
target = 'abc95666hhii92'
mat = pat1.search(target)
print(dir(mat))

if mat:
    print ("It matched ...", mat.group(0))
else:
    print ("No match")

'''dot match'''
pat1 = re.compile('(.+)([0-9]+)') #same can be achieved using *
target = 'abc95666hhii92re'
mat = pat1.search(target)
#print(dir(mat))

#When you want to match from right, put .* in the left
if mat:
    print ("It matched ...", mat.group(0))
    print ("It matched ...", mat.group(1)) #Matches from RHS till the num is found...
    print ("It matched ...", mat.group(2))#2
else:
    print ("No match")
'''email match'''

#pat1 = re.compile('([a-z0-9_]+)@(.+)')
target = 'abc_1234@hotstar.comkil'
match = pat1.search(target)
if match:
    print ("Mail id matched ", match.group(0)) # entire mail id
    print ("Mail matched ", match.group(1)) #username
    print ("Mail matched ", match.group((2))) # domain name
else:
    print ("Mail not matched")

'''Exactly 10 digit match'''
pat1 = re.compile('^[0-9]{10}$') #From starting to ending should be ten digits
cell = '7987967789'
if pat1.search(cell):
    print ("it matched")
else:
    print ("Not matched")