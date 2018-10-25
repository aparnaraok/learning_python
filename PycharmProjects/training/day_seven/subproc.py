import os
import subprocess
completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)
#print('returncode:', completed.stdout.decode('utf-8'))

#print ("Type is ", type(completed))

#du -sh
#print ("completed>>>>", completed)
#print (os.stat(completed))

#Calculates the dir tree size
# size = subprocess.run(['du', '-sh'])
# print ("SSIZE>>>", size)

'''
cwd = os.getcwd()
siz = os.stat(cwd)

print (" dcaggfa")
print (siz[6])
'''

import subprocess

completed = subprocess.run(
    ['ls', '-1'],
    stdout=subprocess.PIPE,
)
# print('returncode:', completed.returncode)
# print('Have {} bytes in stdout:\n{}'.format(
#     len(completed.stdout),
#     completed.stdout.decode('utf-8'))
# )
#print (completed.stdout.split('\n'))

a = completed.stdout.decode('utf-8')
a = a.strip().split("\n")

size = 0
for file in a:
    size += os.stat(file)[6]
print ("Files size>>>", size)


# alter.txt
# dict_oper.py
# dict_set.py
# file_dup.py
# __init__.py
# ip_addr.py
# matrix_mul.py
# mat_transpose.py
# mod1.txt
# mod.txt
# names.txt
# notes.txt
# os_ex.py
# __pycache__
# stdin_ex.py
# subproc.py
# Files size>>> 11300
