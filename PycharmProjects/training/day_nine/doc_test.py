import doctest

def my_function(a, b):
    """   >>my_function(2,3)
    6
    >>my_function('a',3)
    'aaa'
    """

    return a * b

#print (my_function(2,3))
#print (my_function('b', 3))

#Instead of gng to command line..try this

if __name__ == "__main__":
    doctest.testmod(verbose=True)

# Run in terminal:
#
# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_nine$ python -m doctest -v doc_test.py
# 6
# aaa
# 2 items had no tests:
#     doc_test
#     doc_test.my_function
# 0 tests in 2 items.
# 0 passed and 0 failed.
# Test passed.




#using doctest

# 6
# bbb
# 2 items had no tests:
#     __main__
#     __main__.my_function
# 0 tests in 2 items.
# 0 passed and 0 failed.
# Test passed.