#lists in to one list
lis = [[1,2],[3,[5,6]],7]
lis1 = []

def listInlist(lis):
    for var in lis:
        if type(var) is list:
            listInlist ( var )
        else:
            lis1.append ( var )
    return lis1

print(listInlist(lis))

#index of a element in lists

ele = int(input("enter the element"))
a =[]
b = 0
def indexList(lis,ele):
    global a
    global b
    for var in lis:
        if type(var) is list and len(var) >= 0:
            a.append(lis.index(var))
            indexList ( var ,ele)
            if b==0 :
                a = [ ]

        elif ele == var:
             b = ele
             a.append ( lis.index ( var ) )
        if b != 0:
            break
    return a
print(indexList(lis,ele))
