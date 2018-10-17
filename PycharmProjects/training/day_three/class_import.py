#Importing the Student class from the class_ex module

import copy
from class_ex import Student

stu1 = Student('Sam',-22)
stu2 = Student('Kam', 12)
#stu3 = stu1 #changes as per stu1
stu3 = copy.deepcopy(stu1) #constructor is not initialised while creating deep copies..so no change in value occurs
#print (stu1.name + "'s age is ", stu1.age
print (stu1.get_name() + "'s age is ", stu1.get_age())
print (stu2.get_name() + "'s age is ", stu2.get_age())
print (stu1.get_name() + "'s roll num is ", stu1.get_roll())
stu1.inc_age(3)
print ("After incrementing the age.......")
print (stu1.get_name() + "'s age is ", stu1.get_age())
print (stu2.get_name() + "'s age is ", stu2.get_age())
print (" ")
print ("The value of stu3 is .......")
print (stu3.get_name() + "'s age is ", stu3.get_age())

print (stu1.get_roll())
print (stu3.get_roll())
print (stu2.get_roll())

print ("Object of student>>>>>", stu1) #__repr__ is invoked from class Student

print (stu1 > stu2)
print (5 > 7)