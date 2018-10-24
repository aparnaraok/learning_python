class MyInt(type):
    #type is a class
    #int(5)
    #type(int)....type...class
    #self can be replaced by cls and vice versa
    def __call__(self, *args, **kwargs):
        print ("****Here is my int******", args)
        print ("Now do whatever you want with these objects")
        print(">>>>>>>>", type.__call__(self, *args, *kwargs))

        return type.__call__(self, *args, *kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)
print ("I>>>>>", i)

#output
#>>>>>>>> <__main__.int object at 0x7ffb32c27a58>
#I>>>>> <__main__.int object at 0x7ffb32c27a20>