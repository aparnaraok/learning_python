import doctest

class MyClass:
    pass # do nothing

def myfunc(obj):
    '''
    >>> myfunc(MyClass()) #doctest: +ELLIPSIS
    <__main__.MyClass object at 0x...>
    '''
    return obj

if __name__ == '__main__':
    doctest.testmod(verbose=True)

# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_nine$ python stud_class_test.py
# Trying:
#     myfunc(MyClass()) #doctest: +ELLIPSIS
# Expecting:
#     <__main__.MyClass object at 0x...>
# ok
# 2 items had no tests:
#     __main__
#     __main__.MyClass
# 1 items passed all tests:
#    1 tests in __main__.myfunc
# 1 tests in 3 items.
# 1 passed and 0 failed.
# Test passed.
