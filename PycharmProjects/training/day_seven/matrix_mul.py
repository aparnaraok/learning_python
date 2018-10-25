#create a func accepting 2 args
#one is list and other is tuple
#product of the elements in the tuple should be eq to len(list)

#eg : [1,2,3,4,5,6],(2,3)
#output : [[1,2,3], [4,5,6]]

#eg2 : [1,2,3,4,5,6], (3,2)
#output : [[1,2], [3,4], [5,6]]

def mat_form(lis, tu):
    new_list = []
    lis1 = []
    lis2 =[]
    try:
        length = len(lis)
        prod = tu[0] * tu[1]
        if length == prod:
            print ("length is >>>", length)
            print ("product is >>>", prod)

            for i in range(0, tu[1]):
                print (lis[i])
                lis1.append(lis[i])
                #new_list.append(lis1)
            for j in range(tu[1], len(lis)):
                print (lis[j])
                lis2.append(lis[j])
                #new_list.append(lis2)
            new_list.append((lis1))
            new_list.append(lis2)
    except Exception as e:
        print ("Exception", e)
    return  new_list
lis = [1,2,3,4,5,6]
tu = (3,2)
new_list = mat_form(lis, tu)
print ("new list", new_list)

#output
#new list [[1, 2, 3], [4, 5, 6]]
