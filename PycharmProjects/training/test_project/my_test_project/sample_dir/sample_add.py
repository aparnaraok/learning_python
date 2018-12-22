#-----------------------------------------------------------------------
#File to add two numbers
#-----------------------------------------------------------------------

class SampleAdd(object):
    def __init__(self, a, b):
         print("Initializing...................")
         self.a = a
         self.b = b
    def add(self):
        #rint("Adding two numbers......")
        print(self.a + self.b)
        return (self.a + self.b)

    def sub(self):
       # rint("Adding two numbers......")
       print(abs(self.a - self.b))
       return (abs(self.a - self.b))
    #
#
# if __name__ == '__main__':
#     sample_add = SampleAdd(10,20)
#     print(sample_add.add())