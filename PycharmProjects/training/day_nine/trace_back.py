import doctest
#When we expect the exact output as specified in the docstring.
#If we want to capture the exception at the exact point in the earlier stage...we use this sort of func

def this_raises():
    """This function always raises an exception.
    >>> this_raises()
    Traceback (most recent call last):
    RuntimeError: Here is the error
    """
    raise RuntimeError('Here is the error')

if __name__ == '__main__':
    print (this_raises.__doc__)
    doctest.testmod(verbose=True)

# Traceback (most recent call last):
#   File "/home/cisco/PycharmProjects/training/day_nine/trace_back.py", line 7, in <module>
#     raise RuntimeError('Here is the error')
# RuntimeError: Here is the error


# This function always raises an exception.
#     >>> this_raises()
#     Traceback (most recent call last):
#     RuntimeError: Here is the error


# Trying:
#     this_raises()
# Expecting:
#     Traceback (most recent call last):
#     RuntimeError: Here is the error
# ok
# 1 items had no tests:
#     __main__
# 1 items passed all tests:
#    1 tests in __main__.this_raises
# 1 tests in 2 items.
# 1 passed and 0 failed.
#Test passed.