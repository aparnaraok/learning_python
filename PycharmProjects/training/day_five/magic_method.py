class A(object):

    def __new__(cls):
        print ("A.__new__ called")
        return super(A, cls).__new__(cls)

    def __init__(self):
        print ("A.__init__ called")  # -> is actually never called

#print (A())
obj = A()
print (obj)

#If new is not returning, init is not called
#objetc is initialises whenever the new returns something