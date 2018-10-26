from socket import *
s = socket(AF_INET, SOCK_DGRAM) #create datagram socket
msg = b"Hello...Welcome to the world of Python Networking"


#s.sendto(msg, ("", 10000))
s.sendto(msg,("127.0.0.1", 10001))
data, addr = s.recvfrom(16)

print (data)

#change only in server side to upper case and not in client
#data : returned data
#addr : remote address


#First run udp_server.py
#then run udp client in othe terminal
#prints welcome to python