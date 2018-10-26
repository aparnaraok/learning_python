import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9001)) #bind the socket to some port 9001
s.listen(5) #size of the queue is 5
s.settimeout(5)
while True:
    print("Hello ...entered the loop")
    print (s.accept.__doc__)

    c, a = s.accept()
    #print (s.accept.__doc__)
    print ("Received connection from  :  :", a)
    c.send(b"Hello "+bytes(a[0],'utf-8'))
    c.close()

#>>>telnet 127.0.0.1 9001

# cisco@cisco-ThinkPad-T430:~$ netstat -a | grep 9001
# tcp        0      0 localhost:9001          localhost:59670         TIME_WAIT


# cisco@cisco-ThinkPad-T430:~$ telnet 127.0.0.1 9001
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# Hello 127.0.0.1Connection closed by foreign host.


#s is bind listen and acept
#c does everyr\thin...client socket
#a is tup
#waiting state only 5 allowed whereas connecctions are 32 allowed in server
#others are rejected
#unless 1st is processed, 6th cant enter.

#s.set_timeout.__doc__
