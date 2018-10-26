import _thread
import time

def print_time(delay):
    while 1:
        time.sleep(delay)
        print (time.ctime(time.time()))


_thread.start_new(print_time(5,)) #delayed by 5 secs
while(1):
    pass