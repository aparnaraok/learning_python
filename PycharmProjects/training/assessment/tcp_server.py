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


st = ServerTransfer()
st.pass_content()



#Run the python tcp_socket_server.py in terminal

#Run the tcp_server.py

# Initializing print...
# 226 Transfer complete
# Length of files >>> 42
# ['-rw-r--r--   1 ftp      ftp        360448 Mar  1  2013 accessP&S_OTD.zip', 'drwxr-xr-x   2 ftp      ftp          4096 Apr 10  2006 andrews', 'drwxr-xr-x   2 ftp      ftp          4096 Sep  2  2006 avs', 'drwxr-xr-x   2 ftp      ftp          4096 May 15  1996 bibliography', 'drwxr-xr-x   2 ftp      ftp          4096 Dec 13  2002 calendar', 'drwxr-xr-x   2 ftp      ftp          4096 Aug  2  2001 cd_updates', 'drwxrwxr-x   2 ftp      ftp          4096 Feb 28  2006 college', 'drwxrwxr-x   8 ftp      ftp          4096 Mar 24  2001 conference', 'drwxrwxr-x   3 ftp      ftp          4096 Jun 14  1999 convention', 'drwxr-xr-x   3 ftp      ftp          4096 Jan 17  1997 davenport', 'drwxrwxr-x   2 ftp      ftp          4096 Mar 20  2003 dblite', 'drwxr-xr-x   2 ftp      ftp          4096 Nov 21  2005 docbook', 'drwxr-xr-x   2 ftp      ftp          4096 Mar 27  2000 dsssl', 'drwxrwxr-x   2 ftp      ftp          8192 Oct 26 09:55 ephemeral', 'drwxr-xr-x 5309 ftp      ftp        462848 Aug  1  2017 examples', 'drwxrwxr-x   2 ftp      ftp          4096 Mar  5  2002 fox', 'drwxr-xr-x   7 ftp      ftp          4096 Jan 31  1996 frame', 'drwxr-xr-x   3 ftp      ftp          4096 Jun  2  1996 freebooks', 'drwxrwxr-x   3 ftp      ftp          4096 Mar 19  2001 gmat', 'drwxrwxr-x  10 ftp      ftp          4096 Aug 22  2002 graphics', 'drwxr-xr-x   2 ftp      ftp          4096 Dec 29  2004 ind', '-rw-rw-r--   1 ftp      ftp           980 Apr  8  1998 Index', 'drwxr-xr-x   6 ftp      ftp          4096 Mar 16  2006 Intl', 'drwxr-xr-x   3 ftp      ftp          8192 Jun  6  2002 labs', 'drwxrwxr-x   2 ftp      ftp          4096 Apr  1  2003 motif', 'drwxrwxr-x   2 ftp      ftp          4096 Jun  7  2000 multimedia', 'drwxrwxr-x   2 ftp      ftp          4096 Apr  1  2003 openlook', 'drwxr-xr-x   2 ftp      ftp          4096 Jun 21  2001 perlcd', 'drwxrwxr-x   2 ftp      ftp          8192 Jul 17  2006 pod', 'drwxr-xr-x   2 ftp      ftp          4096 Jan 25  2001 poster', 'drwxrwxr-x   3 ftp      ftp          4096 Jun  4  1998 products', '-rw-rw-r--   1 ftp      ftp          2273 Apr  8  1998 README.ftp', 'drwxrwxr-x   2 ftp      ftp          4096 Nov 19  2009 rights', 'drwxr-xr-x   2 ftp      ftp          4096 Apr 12  2006 shortcuts', 'drwxrwxr-x   2 ftp      ftp          4096 Aug 15  2000 soundfiles', 'drwxrwxr-x   2 ftp      ftp          4096 Jul 22  2010 stylesheet', 'drwxr-xr-x   2 ftp      ftp          4096 Mar 24  2006 summit', '-rwx------   1 ftp      ftp         32768 Sep 16  2013 TDIwC2e.pdf', 'drwxr-xr-x   3 ftp      ftp          4096 Nov  4  1998 techreview', 'drwxr-xr-x   2 ftp      ftp          4096 Apr 21  2006 tmp', 'drwxrwxr-x   4 ftp      ftp          4096 Nov 28  2002 utp', 'drwxr-xr-x   2 ftp      ftp          4096 Aug 11  2000 xml']
# Current working dir>>> /home/cisco/PycharmProjects/training/assessment
# filename  -rw-rw-r--   1 ftp      ftp          2273 Apr  8  1998 README.ftp
# Successfully downloaded the  README file
# Initializing print...
# Initialized Server Transfer
# Str content>> Four Debian releases are available on the main site: Testing, or buster.  Access this release through dists/testing.  The Unstable, or sid.  Access this release through dists/unstable.  The --- Other directories: indices         Various indices of the site. project         Experimental packages and other miscellaneous files.
# Data is  FOUR DEBIAN RELEASES ARE AVAILABLE ON THE MAIN SITE: TESTING, OR BUSTER.  ACCESS THIS RELEASE THROUGH DISTS/TESTING.  THE UNSTABLE, OR SID.  ACCESS THIS RELEASE THROUGH DISTS/UNSTABLE.  THE --- OTHER
# Output file successfully created......
