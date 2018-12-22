import os
import paramiko

#Automated way for SCP transfer.
#scp <filename> cisco@localhost:/tmp

def printTotals(transferred, toBeTransferred):
    print ("Transferred : {0}\tOut of : {1}".format(transferred, toBeTransferred))


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)#automating the user input YES
ssh.connect(hostname='localhost', username="cisco", password="cisco", port='22')
sftp = ssh.open_sftp() #secure file transfer
localpath = 'hello.py'
remotepath = '/tmp/name.py' #hello.py renames to name.py#dest filename needs to be specified
#sftp.put(localpath, remotepath)
sftp.put(localpath, remotepath, callback=printTotals) #invokes the transfer function
sftp.close()
ssh.close()

#Create a hello.py file in the CWD.
#Transferred : 20	Out of : 20
