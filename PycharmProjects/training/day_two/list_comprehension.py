li = [('a', 1), ('b', 2), ('c', 3)]
lis = [n * 3 for (x,n) in li]
print (lis)

def subtract(a, b):
    return a - b
lis = [(1,2),(2,3),(3,4)]
lis1 = [subtract(y, x) for (x,y) in lis]
print(lis1)


print (list(range(1,10)))
print (list(range(3,10,3)))

lis3 = [[x ** 2 for x in range(i-3, i)] for i in range(3,10,3)]
print (lis3)

lis3 = [[x ** 2 for x in range(i-4, i)] for i in range(4,17,4)]
print (lis3)


li = [1,2,3,4]

li2 = [elem * 2 for elem in [item+1 for item in li]]
print (li2)