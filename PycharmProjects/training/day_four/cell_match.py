import re

pat1 = re.compile('^(\+91|\+44)?[0-9]{8,10}$') #The ? refers to the data (+91) enclosed in the ()
cell = input("Enter cell num")
if pat1.search(cell):
    print ("cell num matched")
else:
    print ("Cell not matched")

country = re.compile('(in|jp|uk)$')