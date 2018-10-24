#Decorator as a class

class myDecorator:
    def __init__(self, f):
         print ("A logging is about to start")
         f()
    def __call__(self):
        print ("Done")

@myDecorator

def myfunct():
    print ("The decorator function called")

myfunct()

# output
# A logging is about to start
# The decorator function called
# Done