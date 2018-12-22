import unittest

class Student:
    pass

#Assert instance takes object and class
class AssertTest(unittest.TestCase):
    def testassert(self):
        self.assertIsInstance(s1, Student)#Throws error if we give some other instance

s1 = Student()
if __name__ == '__main__':
    unittest.main()


# E
# ======================================================================
# ERROR: testassert (__main__.AssertTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/cisco/PycharmProjects/training/day_nine/assert_instance.py", line 9, in testassert
#     self.assertIsInstance(s, Student)
# NameError: name 's' is not defined
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# FAILED (errors=1)
#
# Process finished with exit code 1
