greet = 'good evening'
print ("Title is  : : >>>>", greet.title())
print ("Upper case is : : >>>>>", greet.upper())
print ("Capitalized string is : : >>>>", greet.capitalize())



string = 'abcdefghijklmnopqrstuvwxyz'
print(string[23:4:-1])


print ("hello", end = ' ')
print ("world")
print ("hello", "world", sep = ':')

x = "abcd"
y = 123

string  = "%shello%d"%(x, y)
print ("String>>", string)



print (":%-10s:%10s:" %(x, y))

li = ['abc', 'def', 'ghij']
print (";". join(li))

lis = "abc;def;ghij".split(";")
print(lis)