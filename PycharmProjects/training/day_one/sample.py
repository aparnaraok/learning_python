#Training sample

print ("Hello World...")

x = 23.5
y = 18
z = "Hello"
if x < y:
    print ("okay")
print ("Done")
print ("Type of x is : : ", type(x))
print ("Type of z is : : ", type(z))

print ('"Hello", he said')
print ("'Hello', he said")
print ('''"Hello's , he said"''')
print (r"Hello to Python\n world")

if type(x) is float:
    print ("x is float")
else:
    print ("Something else")

#help("keywords")

x = 15
w = x
x = "Hello"
#w = x

print ("Id of x :  :", id(x), x)
print ("Id of w :  : ", id(w), w)


a, b = 10, 15
print ("The val of a :  :" , a)
print ("The val of b : : ", b)
b, a = a, b
print ("The val of a : : ", a)
print ("The val of b : : ", b)

tup1 = (12,3.12,'hello',[1,2],-14,1.21,10,'world')
print ("Tuple is : : ", tup1)

li1 = [12,3.12,'hello',[1,2],-14,1.21,10,'world']
print ("List is : : ", li1)
