from copy import deepcopy
from assessment.main_stud_class import Student
stu1 = Student("abc")
stu2 = Student("bca")

print(Student.get_name(stu1)+"'s age is",Student.get_age(stu1))
print(Student.get_name(stu2)+"'s age is",Student.get_age(stu2))

stu1 = Student("ddd")
#In class explaination
print(stu1.get_name()+"'s age is",stu1.get_age())
print(stu2.get_name()+"'s age is",stu2.get_age())

# print(stu1.name + "'s age is ", stu1.age)
# print(stu2.name + "'s age is ", stu2.age)

stu1.inc_get(3)
print(stu1.get_name()+"'s age is",stu1.get_age())
print(stu2.get_name()+"'s age is",stu2.get_age())

stu3 = deepcopy(stu1)
print(stu3.get_name()+"'s age is",stu3.get_age())

print(stu1.get_roll())
print(stu3.get_roll())
print(stu2.get_roll())
print(stu2.__repr__())
print(stu3.__repr__())
print(stu1.__repr__())
print(str(stu1))
print(stu1.__gt__(stu2))
print(stu1.__eq__(stu3))
# class - second program
# from Third_Day.sample_class import Sample
# a = Sample()
# a.increment()
# print(a.__class__.x)

#storing an object in a file
import pickle
f = open("student.bin","wb")
pickle.dump(stu1,f)
f.close()

#reading an object from a file
f = open("student.bin","rb")
stu5 = pickle.load(f)
print(stu5.get_name()+"'s age is",stu5.get_age())