import logging
import ftplib
import os
import socket
import paramiko

def sample_dec(f):
    def main_dec(*args,**kwargs):
        ret = f(*args)
        logging.info(f.__doc__)
        return ret
    return main_dec

LOG_FILE = 'logging_example.out'
logging.basicConfig(
        filename=LOG_FILE,
        level=logging.DEBUG)
@sample_dec
def get_content_list():
    '''Scans the README file'''
    with open('README.txt') as fhandle:
        content_list = fhandle.readlines()

    content_list = [line.strip() for line in content_list]

    return content_list

@sample_dec
def scan_content():
    '''Returns THE content list'''
    the_content_list = []
    content_list = get_content_list()
    the_list = ['The', 'the']
    for line in content_list:
        content = line.strip()
        for the_line in the_list:
            if the_line in content:
                the_content_list.append(content)
    print("Scan content",the_content_list)
    return the_content_list

@sample_dec
def download_read_me_file():
    '''Downloads the readme file'''
    #f = ftplib.FTP("ftp.gnu.org", "anonymous", "appurao@gmail.com")
    f = ftplib.FTP("ftp.oreilly.com", "anonymous", "appurao@gmail.com")
    #f = ftplib.FTP("ftp.debian.org", "anonymous", "appurao@gmail.com")

    f.cwd('pub')
    #f.cwd('debian')
    files = []
    print(f.retrlines("LIST", files.append))

    print("Length of files >>>", len(files))
    print(files)

    print ("Current working dir>>>", os.getcwd())
    for file_name in files:
        if file_name.endswith('ftp'):
            print("filename ", file_name)
            #f.retrbinary('RETR README', open('README.txt', 'wb').write)

            print ("Successfully downloaded the  README file")
    return True
@sample_dec
def pass_content():
    '''Passess the content to the server'''
    filtered_content = scan_content()
    #print (filtered_content)
    str_content = (' '.join(filtered_content))
    print("Str content>>", str_content)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9001)
    sock.connect(server_address)
    sock.send(bytes(str_content, 'utf-8')) #sending to server
    data, addr = sock.recvfrom(200) #Receiving from server
    data = data.decode('utf-8')
    print ("Data is ",data)

    with open ('output_data.txt', 'w') as fhandle:
        fhandle.write(data)
    print ("Output file successfully created......")
    return data

@sample_dec
def copy_content():
    '''Copies the content'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # automating the user input YES
    ssh.connect(hostname='localhost', username="cisco", password="cisco", port='22')
    sftp = ssh.open_sftp()  # secure file transfer
    localpath = 'output_data.txt'
    remotepath = '/tmp/name.txt'  # hello.py renames to name.py#dest filename needs to be specified
    # sftp.put(localpath, remotepath)
    sftp.put(localpath, remotepath)  # invokes the transfer function
    sftp.close()
    ssh.close()
    print("Successfully copied...")

if __name__ == '__main__':
    if download_read_me_file():
        pass_content()
        copy_content()


#file_obj = FileTransfer()
#file_obj.main()