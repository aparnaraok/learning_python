import sys
def divide():
    x = int(input("enter divisor : "))
    y = int(input("Enter dividend  :  :"))
    print (y/x)
    return y/x
try:
    divide()
except:
    print(sys.exc_info()[0])