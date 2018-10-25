import signal
import time
def alarm_handler(a,b):
    print("Alarm raised",time.ctime())

signal.signal(signal.SIGALRM,alarm_handler)
signal.alarm(4)
print("current time",time.ctime())
time.sleep(6)

