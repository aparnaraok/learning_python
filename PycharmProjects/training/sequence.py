tup1 = (12,3.12,'hello',[1,2],-14,1.21,10,'world')
print ("Tuple is : : ", tup1)

li1 = [12,3.12,'hello',(1,2),-14,1.21,10,'world']
print ("List is : : ", li1)

print ("First ele of tup is :  :", tup1[0])
print ("Last ele of list is : : ", li1[-1])

print (li1[1:4])
print (li1[5:1])
print(tup1[1:-5])
print (li1[1:20])
print ("Last three ele ",tup1[-3:])
print ("First three ele : ", li1[:3])
print (li1[1:-1])

li2 =li1
li3 = li1[:]

print ("li1 is ", id(li1), li1)
print ("li2 is ", id(li2), li2)
print ("li3 is ", id(li3), li3)

print ("li1 is li2", li1 is li2)
print ("li1 is li3", li1 is li3)

print (li1.count.__doc__) #Returns the documentation for count

alphas = "abcdefghijlmnopqrstuvwxyz"
print (alphas[3:24:2])
print (alphas[24:3:-1])
print ("Alphas", alphas[24:3:-2])
print ("Alphas 1....", alphas[1:5])
print ("Alphas 2....", alphas[5:1])


##if [m:n] m

#Palindrome check
pal = "able was i ere i saw elba"
if pal == pal[::-1]:
    print ("it is palindrome")
else:
    print ("Not a palindrome")

print (1 in li1[3])

#+ Operator

l1 = [1,2,3]
l2 = [4,5,6]
print (l1 + l2)

t1 = (1,2,3)
t2 = (4,5,6)
print (t1 + t2)

s1 = "hello"
s2 = "python"
print (s1 + " " + s2)

# The * operator

print (l1 * 3)
print (t1 * 3)
print (s1 * 3)

