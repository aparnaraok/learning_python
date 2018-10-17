x,y,z = 5,10,15
print (x > 6 and y < 12 or z < 16) # and preceded over or

'''
wage = int(input("Enter the wage"))
print ("Daily wage is : : >>>>", wage * 8)
print ("High" if wage > 5000 else "Moderate")
'''


time = int(input("Enter the time"))
print (str(time - 12) + "PM " if time > 12 else str(time) + "AM")

x = 2500
if x == 2500:
    print ("x equals 2500")
elif x == 3500:
    print ("x equals 3500")
else:
    print ("x is something else")
