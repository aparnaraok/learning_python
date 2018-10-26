import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.settimeout(20)
print('connecting to localhost')

try:

    # Send data
    message = b'Nive is goood.'
    print('sending {!r}'.format(message))
    sock.sendto(message,('localhost', 30000))

    data,addr = sock.recvfrom(16)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()

#run the server
# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_eight$ python socket_UDP_Upper.py
# starting up on localhost port 30000
# waiting for a connection
#
# received NIVE IS GOOOD.
# sending data back to the client
# finallyy.........
# waiting for a connection
# finallyy.........
