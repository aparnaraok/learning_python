import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 30000)
print('starting up on {} port {}'.format(*server_address))

sock.bind(server_address)
sock.settimeout(20)

while True:
    # Wait for a connection
    print('waiting for a connection')
    try:
        data, addr = sock.recvfrom(16)
        while True:
            p = str(data,encoding='utf-8').upper()
            print()
            print('received {}'.format(p))

            f=bytes(p,encoding='utf-8')
            print('sending data back to the client')
            sock.sendto(f,addr)
            break

    finally:
        # Clean up the connection
        print('finallyy.........')


# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_eight$ python socket_UDP_Upper.py
# starting up on localhost port 30000
# waiting for a connection
#
# received NIVE IS GOOOD.
# sending data back to the client
# finallyy.........
# waiting for a connection
# finallyy.........


