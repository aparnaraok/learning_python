class Repeater:
    def __init__(self, v):
        self.value = v
    def __iter__(self):
        return RepeaterIterator(self) #Returns an object which is source being passed
class RepeaterIterator:
    def __init__(self, s):
        self.source = s
    def __next__(self):
        print ("SOURCE VAL>>>>", self.source.value)
        return self.source.value
        #object.itsownvar.value

rep = Repeater({12,14,16})
print (dir(rep))

#rep_iter = RepeaterIterator(rep)
#print (dir(rep_iter))

'''Infinite loop print since we are not stopping it anywhere'''
# for var in rep:
#     print(var)

iter1 = rep.__iter__()

#while True:
#    item = iter1.__next__()
#    print (item)


print ("NECXT 1" , next(iter1))
print ("Nect 2  :", next(iter1))
item = iter1.__next__()
print ("Next 3>>>>", next(iter1))