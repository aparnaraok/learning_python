import pickle

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

'''
emp = Employee('abc', 20)
print (emp)
print(emp.name)
print(emp.age)

f = open("employee.bin","wb")
pickle.dump(emp,f)
f.close()

print("Contents dumped successfully.....")



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9001)
    sock.connect(server_address)
    sock.send(bytes(str_content, 'utf-8')) #sending to server
    data, addr = sock.recvfrom(200) #Receiving from server
    data = data.decode('utf-8')
    print ("Data is ",data)
'''
