#-----------------------------------------------------------------------
#File to add two numbers
#-----------------------------------------------------------------------

class SampleSub(object):
    def __init__(self, a, b):
         print("Initializing...................")
         self.a = a
         self.b = b


    def sub(self):
       # rint("Adding two numbers......")
       print(abs(self.a - self.b))
       return (abs(self.a - self.b))
