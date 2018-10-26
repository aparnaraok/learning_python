#_thread is a low level module and thus we implement the same using thread class
#_thread has start()
import threading, time

class PrintTime(threading.Thread):
    #threading.Thread is itself a class
    def __init__(self, timer):
        #when we initialize the inherited class we use self
        threading.Thread.__init__(self)
        self.interval = timer
    def run(self): #run method is from threading.Thread
        while True:
            time.sleep(5)
            print (time.ctime(time.time()))
p1 = PrintTime(5)
p1.start() #will invoke run()
while True:
    pass

#prints thread every 5 secs

# Fri Oct 26 17:09:23 2018
# Fri Oct 26 17:09:28 2018
# Fri Oct 26 17:09:33 2018
# Fri Oct 26 17:09:38 2018
# Fri Oct 26 17:09:43 2018
# Fri Oct 26 17:09:48 2018
# Fri Oct 26 17:09:53 2018