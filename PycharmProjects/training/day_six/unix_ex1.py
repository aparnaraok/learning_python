#0-STDIN
#1-STDOUT
#2-STDERR
#3 AND SOON -- FILE DISTRIBUTE NUMBERS CREATED BY OS



import os
# fd = os.open("output.txt",os.O_CREAT|os.O_WRONLY, 644)
# os.write(fd,b"Hello World\n")
# os.close(fd)

fd = os.open("output.txt",os.O_RDONLY)
while True:
    data = os.read(fd,1)
    os.write(1,data)#here 1 indicates stdout
os.close()



