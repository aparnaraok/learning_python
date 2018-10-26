import threading
from time import sleep, time, ctime
#loops = [4,2]
loops = [1,10,30,50,60]
def loop(nloop, nsec):
    print ("start loop ", nloop, 'at', ctime(time()))
    sleep(nsec)
    print ("loop", nloop, 'done at : ', ctime(time()))

def main():
    print ("Starting threads...")
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args = (i, loops[i]))
        threads.append(t)
    for i in nloops: #starts all threads
        threads[i].start()
    for i in nloops:
        threads[i].join() #it waits for all threads to finish whereas os.wait() is the wait time for process
    print ("all DONE at : ", ctime(time()))
if __name__ == '__main__':
    main()

# Starting threads...
# start loop  0 at Fri Oct 26 17:07:00 2018
# start loop  1 at Fri Oct 26 17:07:00 2018
# loop 1 done at :  Fri Oct 26 17:07:02 2018
# loop 0 done at :  Fri Oct 26 17:07:04 2018
# all DONE at :  Fri Oct 26 17:07:04 2018


# Starting threads...
# start loop  0 at Fri Oct 26 17:08:20 2018
# start loop  1 at Fri Oct 26 17:08:20 2018
# start loop  2 at Fri Oct 26 17:08:20 2018
# start loop  3 at Fri Oct 26 17:08:20 2018
# start loop  4 at Fri Oct 26 17:08:20 2018
# loop 0 done at :  Fri Oct 26 17:08:21 2018
# loop 1 done at :  Fri Oct 26 17:08:30 2018
