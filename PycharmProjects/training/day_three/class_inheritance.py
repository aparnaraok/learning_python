#from class_ex import Student #couldn't be accessed as Student is private class

class Student:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def get_age(self):
        return  self.age

class child_student(Student):
    '''A subclass extending Student class'''

    def __init__(self, n, a, s):
        '''Initializing'''
        Student.__init__(self, n, a) # call __init__ for student
        self.section_num = s
        #self.age = a
    def get_age(self): #Redefines get_age method entirely
        print ("Age :  " + str(self.age))

c = child_student("aaa",12, '12')
c.get_age()