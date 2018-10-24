from copy import deepcopy
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
s1 = Singleton()

s2 = Singleton()
s3 = deepcopy(s1)
'''Both are referring to same objects'''
print ("S1 >>>", s1)
print ("S2 >>>", s2)
print ("S3 >>>", s3)#same as s1 even doing deepcopy

#no way of freeing the obj
#if no one is referring to an initializes obj, then obj is free