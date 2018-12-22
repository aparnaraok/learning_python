import ftplib

#>>>ftp ftp.oreilly.com (Refer notes) in terminal

f = ftplib.FTP("ftp.gnu.org", "anonymous", "appurao@gmail.com")
#f = ftplib.FTP("ftp.oreilly.com", "anonymous", "appurao@gmail.com")

files = []
print (f.retrlines("LIST", files.append))

print ("Length of files >>>", len(files))
print (files[0])



# 226 Transfer complete
# Length of files >>> 6
# lrwxrwxrwx   1 ftp      ftp            12 Jun 21  2002 examples -> pub/examples
#
# Process finished with exit code 0
