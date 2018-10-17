def some_math(x, y):
    '''Arbitraty mathematical calculation'''
    global a
    x = 1.9/x + 8.1 * y
    y = 7.6/x + 3.2*(1/2*y)
    a = 2.3*(9/y + x/7.2)
    b = 5.6*x + 7/8*y
    return a + b
al,b = 4.63, 7.81
#res = some_math(a, b)
#print ("Result of the calculation is ", res)

if __name__ == '__main__':
    res = some_math(al, b)
    print ("Result of the calculation is ", res)
    print ("A is ", al)
    print ("b is ", b)
    print ("Id of a ", id(a))

def some_math(x, y):
    '''Arbitraty mathematical calculation'''
    x = 2/x + y
    print ("First x>>>", x)
    y = 4 + y/2
    print ("First y>>>", y)
    x = 4/x + 4/y
    print ("Second x >>", x)
    y = 8/x + 4
    print ("Second y>>>>", y)
    return x + y

a,b = 2,4
if __name__ == '__main__':
    res = some_math(a, b)
    print ("Result of the calculation is %.2f " %res)

print (some_math.__doc__)





def append_ele(li, ele):
    '''Appends the ele to the list'''
    li.append(ele)
    #return li
li1 =[20,100]
if __name__ == '__main__':
    append_ele(li1, 10)
    print ("the final list>>>>", li1)