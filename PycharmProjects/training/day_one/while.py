x = 3
while x < 10:
    print (x ,"still in the loop")
    x = x + 1

x = 6
while x < 5:
    print (x , "still in the loop")
print (x, "not in thr loop")


i = 0
while i < 10:
    i = i + 1
    if i <= 4:
        print ("Continue")
        continue
    print ("The value of i is : : ", i)

    if i >= 8:
        print ("Break")
        break

li1 = [1,2,3,5,7,3,6,10]
for var in li1:
    print (var)

for var in range(len(li1)):
    print (var)