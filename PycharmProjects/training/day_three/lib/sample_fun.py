##__name__ takes the name of the module

def my_add(x, y):
    return x + y
def my_sub(x, y):
    return  x - y

print ("NAME is >>>", __name__)
if __name__ == '__main__':

    lis1 = [1,2,3,4]
    print (lis1)
    print ("From module >>>>", my_add(10,10) )
    print ("From sub module >>>>", my_sub(20,10))