import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10001)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16).upper()
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

#open 2 terminals
#In 1st terminal >>>run..python tcp_echo_client.py
#In 2nd terminam>>> telnet 127.0.0.1 10001



#telnet 127.0.0.1 10001

#In terminal 1:

# cisco@cisco-ThinkPad-T430:~$ telnet 127.0.0.1 10001
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# aparna
# APARNA
# Aparna
# APARNA
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# ^]
# telnet> quit
# Connection closed.

#python tcp_echo_client.py
# sending data back to the client
# received b'APARNA\r\n'
# sending data back to the client
# received b'ABCDEFGHIJKLMNOP'
# sending data back to the client
# received b'QRSTUVWXYZ\r\n'
# sending data back to the client
# received b''
# no data from ('127.0.0.1', 52802)
# waiting for a connection
