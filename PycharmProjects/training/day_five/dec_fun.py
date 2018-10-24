#decorator as a function
#closure ...... a func within another func
def entryExit(f):
    def new_f():
        print ("Entering ", f.__name__)
        f()
        print ("Exited ", f.__name__)
    return  new_f()


@entryExit
def func1():
    print ("Calling the decorator func 1")

# Entering  func1
# Calling the decorator func 1
# Exited  func1

@entryExit
def func2():
    print ("Inside dec fun 2")
# Entering  func1
# Calling the decorator func 1
# Exited  func1
# Entering  func2
# Inside dec fun 2
# Exited  func2

func1()
func2()

print ("Func 1 name >>>>", func1.__name__)

