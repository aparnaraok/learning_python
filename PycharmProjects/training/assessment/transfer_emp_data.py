import pickle
import socket
from sample_class import Employee


def get_class_content():
    '''Returns the object of the Employee class'''
    stu = Employee('abc', 12)
    return stu

def dump_to_file():
    stu_obj = get_class_content()
    #f = open("employee.bin", "wb")
    dump_data =  pickle.dumps(stu_obj)
    print(dump_data)
    #f.close()
    print("Contents dumped successfully...")

    return dump_data
    print("Contents dumped successfully...")
    #rec_from_server(stu_obj.name)

def rec_from_server(str_content):
    '''Receives the data from server'''

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9002)
    sock.connect(server_address)
    #sock.send(bytes(str_content, 'utf-8'))  # sending to server
    sock.send(str_content)  # sending to server
    data = sock.recv(200)  # Receiving from server
    #data = data.decode('utf-8')
    print("Data is ", data)


if __name__ == '__main__':
    dump_data = dump_to_file()
    print("Dump data>>>", dump_data)
    rec_from_server(dump_data)

