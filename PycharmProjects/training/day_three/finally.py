
#in the debugging, finally will be executed and can't be escaped
#Files temporarily created would be deleted
#Finally will be executed in case of raise too whereas the global code part will not get executed once the exception is raised using raise
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print ("division by zero !")
    else:
        print ("Result is  :  :", result)
    finally:
        print ("executing finally clause")
divide(6,3)
