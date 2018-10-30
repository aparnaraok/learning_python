import os

print("Before fork", os.getpid())

s = os.fork()

if s == 0:
    print("I am child", os.getpid())
    print("I am child, parent id is", os.getppid())

else:
    print("I am parent, my pid is", os.getpid())
    print("My child is", s)
    
