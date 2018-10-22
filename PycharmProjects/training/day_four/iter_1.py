ilist = (iter(['some', 'list']))
print("Ilist object>>>>", ilist)
print (next(ilist))  #some
print (next(ilist))  #list

print (" ")
iset = (iter({'some', 'set'}))
print("Iset object>>>>", iset)
print (next(iset))  #set
print (next(iset))  #some

print (" ")
istr = (iter('some string'))
print("Istring object>>>>", istr)
print (next(istr))  #s
print (next(istr))  #o