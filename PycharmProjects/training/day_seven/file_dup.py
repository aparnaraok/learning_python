import sys
import os

divisor = int(input(" "))
dividend = int(input(" "))

fd = os.open("alter.txt", os.O_CREAT|os.O_WRONLY)
os.dup2(fd, 2)

if divisor == 0:
    sys.stderr.write("Can't divide by zero")
os.close(fd)

#python file_dup.py
#cat alter.txt
#Can't divide by zerocisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_seven$
#stderr captures the error in the console
#stdout captures the output in the console