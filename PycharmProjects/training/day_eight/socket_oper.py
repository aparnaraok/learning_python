import socket
hname = socket.gethostname()
print ("hostname >>>", hname)

get_host_by_name = socket.gethostbyname('www.python.org')
print ("The name of the host is ", get_host_by_name)

get_host_by_addr = socket.gethostbyaddr(b'151.101.156.223')
print (get_host_by_addr)

# hostname >>> cisco-ThinkPad-T430
# The name of the host is  151.101.156.223
# Traceback (most recent call last):
#   File "/home/cisco/PycharmProjects/training/day_eight/socket_oper.py", line 8, in <module>
#     get_host_by_addr = socket.gethostbyaddr(b'151.101.156.223')
# socket.herror: [Errno 1] Unknown host
