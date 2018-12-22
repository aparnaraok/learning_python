#class Name should have Test at the end with capital T
#fun name should start with test with small t

import sys
import matlib
import unittest
class MathTest(unittest.TestCase):
    def testadd(self):
        #self.assertTrue(matlib.myadd(2,3) == 5)
        self.assertEqual(matlib.myadd(2,3) , 5)

    #with no test func
    def hello(self):
        return True
    #def testsub(self):
    #    self.assertTrue(matlib.mysub(8,2) == 6)

    #Testing for incorrectness
    #def testnotadd(self):
    #    return self.assertNotEqual(matlib.myadd(3,2), 6)
class SubTest(unittest.TestCase):
    def testsub(self):
        print ("Sub")
        #self.assertTrue(matlib.mysub(8,2) == 6)
        self.assertEqual(matlib.mysub(2,3) == -1)

    # Testing for incorrectness
    def testnotadd(self):
        return self.assertNotEqual(matlib.myadd(3, 2), 6)

if __name__ == '__main__':
    #no need to create object of the class
    #unittest.main() #checks for the class names ending with Test and creates an object and invokes all the funcs beginning with word "test" with the help of the created objects
    suite = unittest.TestLoader().loadTestsFromTestCase(MathTest)
    unittest.TextTestRunner(verbosity=3).run(suite) # 2/3 both same specifies levels of data to be shown

print (dir(unittest.TestCase))

# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
#
# Process finished with exit code 0


#Failed tc

# F
# ======================================================================
# FAIL: testadd (__main__.MathTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/cisco/PycharmProjects/training/day_nine/unit_test_ex.py", line 9, in testadd
#     self.assertTrue(matlib.myadd(2,8) == 5)
# AssertionError: False is not true
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# FAILED (failures=1)
#
# Process finished with exit code 1



#2 testcase....if one fails...entire test fails

# F.
# ======================================================================
# FAIL: testadd (__main__.MathTest)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/cisco/PycharmProjects/training/day_nine/unit_test_ex.py", line 9, in testadd
#     self.assertTrue(matlib.myadd(2,8) == 5)
# AssertionError: False is not true
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# FAILED (failures=1)


#2 testcase pass:
# /home/cisco/PycharmProjects/training/venv/bin/python /home/cisco/PycharmProjects/training/day_nine/unit_test_ex.py
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
#
# Process finished with exit code 0



###########################verbose##################
# testadd (__main__.MathTest) ... ok
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# OK
# testadd (__main__.MathTest) ... ok
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# OK
#
# Process finished with exit code 0



# testadd (__main__.MathTest) ... ok
# testnotadd (__main__.MathTest) ... ok
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
#
# OK
#
# Process finished with exit code 0


#testing for correction (Equal) should be in one class and testing for incorrectness should be done in other class.
