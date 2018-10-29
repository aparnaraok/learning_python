import doctest

if __name__ == '__main__':
    doctest.testfile('doctest_fun.txt', verbose=True)


# Trying:
#     from doc_test import my_function
# Expecting nothing
# ok
# Trying:
#     my_function(2,3)
# Expecting:
#     6
# ok
# 1 items passed all tests:
#    2 tests in doctest_fun.txt
# 2 tests in 1 items.
# 2 passed and 0 failed.
# Test passed.