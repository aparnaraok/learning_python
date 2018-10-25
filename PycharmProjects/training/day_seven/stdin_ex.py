fname = input("Enter your first name : ")
lname = input("Enter your last name : ")

print ("Your first name is >>>", fname)
print ("Your last name is >>>", lname)


#<     creates a duplicate file descriptor for STDIN (0)

#0 STDIN
#1 STDOUT
#2 STDERR

# cisco@cisco-ThinkPad-T430:~/PycharmProjects/training/day_seven$ python stdin_ex.py < names.txt
# Enter your first name : Enter your last name : Your first name is >>> kota
# Your last name is >>> aparnarao
