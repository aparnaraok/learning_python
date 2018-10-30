import socket
from file_transfer import FileTransfer

class ServerTransfer(FileTransfer):
    def __init__(self):
        '''Initializing'''
        super(ServerTransfer, self).__init__()
        print ("Initialized Server Transfer")
    def pass_content(self):
        '''Passess the content to the server'''

        filtered_content = self.scan_content()
        #print (filtered_content)
        str_content = (' '.join(filtered_content))
        print("Str content>>", str_content)

        #for content in filtered_content:
        #    content = content.strip()
            #print (bytes(content, 'utf-8'))

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 9001))  # bind the socket to some port 9001
        s.listen(5)  # size of the queue is 5
        # s.settimeout(5)
        while True:
            print("Hello ...entered the loop")
            c, a = s.accept()
            print("Received connection from  :  :", a)
            c.send(bytes(str_content, 'utf-8'))
                #c.close()
        self.recv_content()

    def recv_content(self):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = ('localhost', 9001)
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
            except Exception as e:
                print("Unable to connect to server ....", e)
                pass

st = ServerTransfer()
st.pass_content()
#import socket
#import sys
'''
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
    except Exception as e:
        print ("Unable to connect to server ....", e)
        pass
'''
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 9001)) #bind the socket to some port 9001
s.listen(5) #size of the queue is 5
#s.settimeout(5)
while True:
    print("Hello ...entered the loop")
    print (s.accept.__doc__)

    c, a = s.accept()
    #print (s.accept.__doc__)
    print ("Received connection from  :  :", a)
    c.send(b"Hello "+bytes(a[0],'utf-8'))
    c.close()
'''