import pdb

def some_div(some_int):
    print ("Start int ", some_int)
    ret_int = 10/some_int
    print("End some int", some_int)
    return ret_int
#pdb.run("some_div(2)")
#pdb.runeval("some_div(2)") #run_eval ret something
#pdb.run_call(<func name> , parameter)

#post_mortem
if __name__  == "__main__":
    try:
        some_div(0)
    except:
        import sys
        tb = sys.exc_info()[2]
        pdb.post_mortem(tb) #exception is passed as a parameter

#post_mortem #tells about the exception line
# -> ret_int = 10/some_int
# (Pdb) r
#

#some_div(2)
# Start int  2
# End some int 2




# > <string>(1)<module>()
# (Pdb) 10
# 10
# (Pdb) 0
# 0
# (Pdb) 1
# 1
# (Pdb)

# (Pdb) h
#
# Documented commands (type help <topic>):
# ========================================
# EOF    c          d        h         list      q        rv       undisplay
# a      cl         debug    help      ll        quit     s        unt
# alias  clear      disable  ignore    longlist  r        source   until
# args   commands   display  interact  n         restart  step     up
# b      condition  down     j         next      return   tbreak   w
# break  cont       enable   jump      p         retval   u        whatis
# bt     continue   exit     l         pp        run      unalias  where
#
# Miscellaneous help topics:
# ==========================
# pdb  exec
#
#(Pdb)
# (Pdb) r
# Start int  0
# --Return--
# > <string>(1)<module>()->None
# (Pdb)
#
# (Pdb) r
# Traceback (most recent call last):
#   File "/home/cisco/PycharmProjects/training/day_nine/pdb_ex.py", line 8, in <module>
#     pdb.run("some_div(0)")
#   File "/usr/lib/python3.5/pdb.py", line 1566, in run
#     Pdb().run(statement, globals, locals)
#   File "/usr/lib/python3.5/bdb.py", line 431, in run
#     exec(cmd, globals, locals)
#   File "<string>", line 1, in <module>
#   File "/home/cisco/PycharmProjects/training/day_nine/pdb_ex.py", line 5, in some_div
#     ret_int = 10/some_int
# ZeroDivisionError: division by zero
#
#Process finished with exit code 1

#--------------
#print returns None
#print(print.__doc__)
#executes line by line until the func returns something>>>>>r
#-------------

#c returns entire



# > <string>(1)<module>()
# (Pdb) c
# Traceback (most recent call last):
#   File "/home/cisco/PycharmProjects/training/day_nine/pdb_ex.py", line 8, in <module>
#     pdb.run("some_div(0)")
#   File "/usr/lib/python3.5/pdb.py", line 1566, in run
#     Pdb().run(statement, globals, locals)
#   File "/usr/lib/python3.5/bdb.py", line 431, in run
# Start int  0
#     exec(cmd, globals, locals)
#   File "<string>", line 1, in <module>
#   File "/home/cisco/PycharmProjects/training/day_nine/pdb_ex.py", line 5, in some_div
#     ret_int = 10/some_int
# ZeroDivisionError: division by zero
#
# Process finished with exit code 1




#pdb.run()returns None always
#h r



#pass 2:
# > <string>(1)<module>()
# (Pdb) r
# Start int  2
# End some int 2
# --Return--
# > <string>(1)<module>()->None
# (Pdb) r

#r means run which ret None

# > <string>(1)<module>()
# (Pdb) c
# Start int  2
# End some int 2



#run_eval

# > <string>(1)<module>()
# (Pdb) r
# Start int  2
# End some int 2
# --Return--
# > <string>(1)<module>()->5.0
# (Pdb) c


