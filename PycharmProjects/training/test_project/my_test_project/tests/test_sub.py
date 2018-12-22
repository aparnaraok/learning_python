#------------------------------------------------------------------
#Test file to add 2 numbers
#------------------------------------------------------------------
import os
import sys
sys.path.append('../')

#import sample_dir.sample_add
from my_test_project.sample_dir.sample_sub import SampleSub
#from my_test_project.sample_dir.sample_add import SampleAdd
print("Import successful..")

def test_0_sub():
   sub_obj = SampleSub(20,30)
   result = sub_obj.sub()
   print("Inside test result>>>>", result)
   assert result == 10

def test_1_add():
   add_obj = SampleAdd(20,30)
   result = add_obj.add()
   print("Inside test result>>>>", result)
   assert result == 50



#test_0_sub()
#test_1_add()