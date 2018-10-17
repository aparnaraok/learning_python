#While creating the class,there will be no object existing.
#so 'self' acts as a placeholder for it.

class Student:
    '''Student class'''
    total = 0
    def __init__(self, n, a):
        '''Initializing'''
        #self.name = n
        self.__name = n
        self.__age = a
        self.__class__.total += 1 #12 seater stop creating objects once the required count is reached
        self.__roll = self.__class__.total #checking using roll no

        try:
            if a < 0:
                raise Exception(a, n)
            else:
                self.__age = a
        except Exception as inst:
            print ("Negative age" , inst.args)
            self.__age = 0
        self.__marks = 0

    def get_age(self):
        '''Returns the age'''
        return self.__age
    def get_name(self):
        '''Returns the name'''
        return self.__name
    def inc_age(self, n):
        '''Increments the age by n'''
        self.__age += n
    def get_roll(self):
        return self.__roll
    def __repr__(self): #Invoked whenever an object is called
        return  "An object of class Student"
    def __gt__(self, other):
        if type(other) is Student:
            return self.__age > other.get_age()
# s = Student()
# print("The age is : : ", s.get_age())
# print ("The name is : : ", s.get_name())
