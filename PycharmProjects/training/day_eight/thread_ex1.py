#process is completely differ ent (parent and child)
#whereas threading is like implementing two funcs at once

import _thread
import time
x = 0
def inc_x(inc):
    global x
    x = x + inc
    print (x)

def print_x(val):
    global x
    print (x + val)

_thread.start_new_thread(inc_x, (8,))
_thread.start_new_thread(print_x, (5,))
#_thread.start_new_thread(print_x, (15,))
#_thread.start_new_thread(print_x, (25,))

#To start the program since creation of the thread alone doesn't start the program
while True:
    pass

# 15
# 5
# 25
# 8