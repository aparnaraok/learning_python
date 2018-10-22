import re
pat1 = re.compile('[fjjb]a?b', re.IGNORECASE)
if pat1.search('BB'):
    print ("It matched")
else:
    print ("Not matched")