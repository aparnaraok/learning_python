A = [[1,2],[3,[4,5]],6]

def append_lis(A):
    lis = []
    for ele in A:
        if type(ele) is list:
            lis = lis + append_lis(ele)
        else:
            lis.append(ele)
    return lis
print (append_lis(A))