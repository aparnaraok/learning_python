class Myclass():
    def __init__(self):
        self.__a = 5
    def getA(self,a):
        return self.__a, a

class Myclass2(Myclass):
    def __init__(self):
        Myclass.__init__(self)
        self.c = 15
        self.__d = 20




m = Myclass()
m.__a = 10
print(m.__a)
print(m.getA(m.__a))


>>> def ADD(a,b):
...     return a+b
...
>>> a = ADD
>>> a(1,2)
3
>>>



To redefine the type class...