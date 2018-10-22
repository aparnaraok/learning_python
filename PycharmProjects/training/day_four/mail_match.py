import re

'''email match'''

#pat1 = re.compile('([a-z0-9_]+)@(.+)')
#pat1 = re.compile('([a-z0-9_]+)@(.+)')
pat1 = re.compile('([a-z0-9_]+)@([a-z]+)(.com$)')


target = 'abc_1234@hotstar.comkkh'
target = 'a123_abcd@gmail.com'
match = pat1.search(target)
if match:
    print ("Mail id matched : :", match.group(0)) # entire mail id
    print ("Mail matched : :", match.group(1)) #username
    print ("Mail matched : :", match.group((2))) # domain name
else:
    print ("Mail not matched : : ", target)