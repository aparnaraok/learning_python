#import socket

#from socket import *

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #create datagram socket
s.bind(("", 10001)) #bind the socket to some port 9001
#s.settimeout(20)

while True:
    data, addr = s.recvfrom(16) #wait for a message
    resp = b"Welcome to Python Networking!!!"
    s.sendto(resp.upper(), addr) #send response

#sockets use transport layer interface sockets
#after accept fork()
#no connection is established
#only sends and receives packets

# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_eight$ python3 udp_server.py
# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_eight$ python3 socket_udp_client_echo.py
# b'WELCOME TO PYTHO'
