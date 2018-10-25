# sleep in python

import os
import sys
import time

pid = os.fork()

# Fork - replicates the process So prints two Hello world
if pid == 0:
    time.sleep(5)
    print("i am child, my parents pid is ", os.getppid())  # get parents pid but because of
    # sleep it becomes orpan and gets a new parent
    print("i am child, my pid is", os.getpid())

else:
    # os.wait()#wait forces the parent to wait
    print("Hello World from parent my pid id is", os.getpid())  # get its own pid
print("Child pid is", pid)  # fork returns the process id of the child in pid

r, w = os.pipe() #pipe opens in read and write mode
pid = os.fork()

if pid:
    os.close(w)
    r = os.fdopen(r)
    print ("Parent reading")
    mstr = r.read()

    print ("text = ", mstr)
    sys.exit(0)
else:
    #This is the child process
    os.close(r)
    w = os.fdopen(w,'w')
    print ("Child writing")
    w.write("Text written by child")
    w.close()
    print ("Child closing")
    sys.exit(0)


# Hello World from parent my pid id is 18335
# Child pid is 18336
# Parent reading
# Child writing
# Child closing
# text =  Text written by child
