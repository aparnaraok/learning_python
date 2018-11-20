#Server code
import pickle
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9002))  # bind the socket to some port 9001
s.listen(5)  # size of the queue is 5
#  s.settimeout(5)
while True:
    print("Hello ...entered the loop")
    c, a = s.accept()   #Accept connection from client
    str_content = c.recv(10000) #Receive data from client
    print("Received connection from  :  :", a)

    print("STR>>>>", str_content)
    str_content1 = pickle.loads(str_content)
    #f = open('employee.bin', 'rb')
    #data = pickle.loads()
    str_name_content = str_content1.name

    print("Str content>>>>>", str_name_content)
    c.send(bytes(str_name_content.upper(),'utf-8')) #Change the content to upper case and send back to client
    #c.send(str_name_content.upper()) #Change the content to upper case and send back to client
    c.close()