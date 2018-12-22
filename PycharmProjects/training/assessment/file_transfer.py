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

        LOG_FILE = 'logging_example.out'
        logging.basicConfig(
            filename = LOG_FILE
            level = logging.DEBUG

        )
    def scan_content(self):
        '''Returns THE content list'''

        the_content_list = []
        content_list = self.get_content_list()
        the_list = ['The', 'the']
        for line in content_list:
            content = line.strip()
            for the_line in the_list:
                if the_line in content:
                    the_content_list.append(content)
        return the_content_list
    def get_content_list(self):
        '''Scans the README file'''
        with open('README.txt') as fhandle:
            content_list = fhandle.readlines()

        content_list = [line.strip() for line in content_list]

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


file_obj = FileTransfer()
file_obj.main()