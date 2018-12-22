#oops -- Class
#self becomes the current class object used to access the memebers and variables in  a class
# to make the variables private write the variable as __variable name(2u)
a=2
class Student:
    total = 0
    global a
    def __init__(self,n):
        self.__name = n
        self.__age = a
        self.__class__.total += 1
        self.__roll = self.__class__.total
        try:
            if a<0:
                raise Exception(a,n)
            else:
                self.__age = a
        except Exception as inst:
            print("negative age",inst.args)
            self.__age = 0

    #getters
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name

    #increment the age
    def inc_get(self,n):
        self.__age +=n

    def get_roll(self):
        return self.__roll

    def __repr__(self):
        return "To Print The User Defined Details Of A Class"

    def __gt__(self,other):
        if type(other) is Student:
            return self.__age > other.get_age()