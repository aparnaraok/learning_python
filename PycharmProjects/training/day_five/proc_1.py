import os
x = 9
pid = os.fork() #fork is a system call which creates/ replicates / new memory by creating a process....creates a cpy of parent
#returns tw0o val in the parent part ret the pid of newly created child and in the child part ret 0
print ("Hello world")

#only one process can be in one memory location
#executes in a processor
#scheduler checks whether all process is taking proper time...if it takes more time...it throws out that process and takes new process
#if process not excecuted,the sche again puts the process into memory and restarts it
#shell creates a copy of it and puts into memory loc and executes process
#new memory/copy is created as a partof command execution

if pid == 0:
    print ("Hello world from child")
    print ("I am child, my parent pid is ", os.getppid())
    print ("I am child...my pid is ", os.getpid())
    #Gets the current pid ...child should match with parent
    x = x+9
    f = open('child_file.txt', 'w')
    f.write(str(x))
    print (" ")
    print ("Child value copied into a file")
    print ("X is ", x)
else:
    #pid of child in the parent part
    os.wait() #Wait till the child gets executed..the child sends a signal to the parent
    print ("Hello world from parent")
    print ("Hello world from parent pid is ", os.getpid())
    print ("PID>>>", pid)
    print ("Parent x is ", x)
    f = open('child_file.txt')
    val = f.read()
    print ("New value from child is ",str(val))
    #if the parent has anything,ot will get reflected in both parent as well as child

# Hello world
# Hello world from parent
# Hello world
# Hello world from child

# Hello world
# Hello world from parent
# Hello world from parent pid is  15230
# PID>>> 15231
# Hello world
# Hello world from child
# I am child, my parent pid is  15230
# I am child...my pid is  15231

#kill -l <sig no 17 is CHLD