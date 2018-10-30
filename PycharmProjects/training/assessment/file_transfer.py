import logging
import ftplib
import os
import re

class FileTransfer(object):
    def __init__(self):
        '''Initializing
        '''
        print ("Initializing print...")
        logging.info("Initializing...")

    def connect_to_server(self):
        '''Connects to server'''

        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 9001))  # bind the socket to some port 9001
        s.listen(5)  # size of the queue is 5
        # s.settimeout(5)
        while True:
            print("Hello ...entered the loop")
            print(s.accept.__doc__)

            c, a = s.accept()
            # print (s.accept.__doc__)
            print("Received connection from  :  :", a)
            c.send(b"Hello " + bytes(a[0], 'utf-8'))
            c.close()
        '''
    def scan_content(self):
        '''Returns THE content list'''

        the_content_list = []
        content_list = self.get_content_list()
        the_list = ['The', 'the']
        for line in content_list:
            content = line.strip()
            #print(content)
            for the_line in the_list:
                if the_line in content:
                    the_content_list.append(content)
            #the_content_list = [content if the_line in content (for the_line in the_list]
        #print(the_content_list)
        return the_content_list
    def get_content_list(self):
        '''Scans the README file'''
        with open('README.txt') as fhandle:
            content_list = fhandle.readlines()
        #print("content list >>>>>", content_list)

        #for line in content_list:
        content_list = [line.strip() for line in content_list]
        #print ("Printing content.....")

        return content_list


    def download_read_me_file(self):
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


    def main(self):
        self.download_read_me_file()
        self.connect_to_server()


file_obj = FileTransfer()
#print (file_obj)
#file_obj.download_read_me_file()
file_obj.main()