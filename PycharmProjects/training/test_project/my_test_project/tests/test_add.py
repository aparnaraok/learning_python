#------------------------------------------------------------------
#Test file to add 2 numbers
#------------------------------------------------------------------
import os
import sys
#sys.path.append('../')

#import sample_dir.sample_add
#from sample_dir.sample_add import SampleAdd
from my_test_project.sample_dir.sample_add import SampleAdd
print("Import successful..")
# #
# class TestAddition(SampleAdd):
#     # def __init__(self):
#     #     print("Initializing the testing of adding 2 nos")
#     def test_0_add(self):
#         add_obj = SampleAdd(10,20)
#         result = add_obj.add()
#         print("Result>>>>", result)
#         assert result == 30
def test_0_add():
   add_obj = SampleAdd(10,20)
   result = add_obj.add()
   print("Inside test result>>>>", result)
   assert result == 30

def test_1_add():
   add_obj = SampleAdd(20,30)
   result = add_obj.add()
   print("Inside test result>>>>", result)
   assert result == 50

def test_0_sub():
   add_obj = SampleAdd(20,30)
   result = add_obj.sub()
   print("Inside test result>>>>", result)
   assert result == 10


#test_0_add()
#test_1_add()
#test_0_sub()