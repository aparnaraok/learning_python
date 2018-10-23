#dir(__builtins__) has Exception

class MyExcept(Exception):
    def __init__(self):
        return
    def __str__(self): #This func is by default accept the exception and print
        print ("My except occured")
def myfunc():
    raise MyExcept

try:
    myfunc()
except:
    print ("Caught an exception")
    raise #generally tells us what the exception has to say

'''Global part'''
#print ("Printed the exception")

#Finally will be executed in case of raise too whereas the global code part will not get executed once the exception is raised using raise
finally:
   print ("Printed final exception")
'''
Output:

Caught an exception
My except occured
Printed final exception #in case of raise
Traceback (most recent call last):
'''