#Server code

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9001))  # bind the socket to some port 9001
s.listen(5)  # size of the queue is 5
#  s.settimeout(5)
while True:
    print("Hello ...entered the loop")
    c, a = s.accept()   #Accept connection from client
    str_content = c.recv(10000) #Receive data from client
    print("Received connection from  :  :", a)
    c.send(str_content.upper() +bytes(a[0] , 'utf-8')) #Change the content to upper case and send back to client
    c.close()