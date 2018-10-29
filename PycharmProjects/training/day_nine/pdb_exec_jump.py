import pdb

def pdb_jump():
    print ("Entered into pdb jump func")
    l1 = [1,2,3,4,5]
    print ("Looping through the list..")
    for var in l1:
        print (var)
pdb.run("pdb_jump()")

# /home/cisco/PycharmProjects/training/venv/bin/python /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py
# > <string>(1)<module>()
# (Pdb) s
# --Call--
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(3)pdb_jump()
# -> def pdb_jump():
# (Pdb) b 5
# Breakpoint 1 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:5
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:5
# (Pdb) b 8
# Breakpoint 2 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:8
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:5
# 2   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:8
# (Pdb) c   ..goes to first brkpoint
# Entered into pdb jump func
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(5)pdb_jump()
# -> l1 = [1,2,3,4,5]
# (Pdb) j 4
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(4)pdb_jump()
# -> print ("Entered into pdb jump func")
# (Pdb) c
# Entered into pdb jump func
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(5)pdb_jump()
# -> l1 = [1,2,3,4,5]
# (Pdb) c
# Looping through the list..
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(8)pdb_jump()
# -> print (var)
# (Pdb) j 7
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(7)pdb_jump()
# -> for var in l1:
# (Pdb) j 5
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(5)pdb_jump()
# -> l1 = [1,2,3,4,5]
# (Pdb) j 8
# *** Jump failed: can't jump into the middle of a block
# (Pdb) l
#   1  	import pdb
#   2
#   3  	def pdb_jump():
#   4  	    print ("Entered into pdb jump func")
#   5 B->	    l1 = [1,2,3,4,5]
#   6  	    print ("Looping through the list..")
#   7  	    for var in l1:
#   8 B	        print (var)
#   9  	pdb.run("pdb_jump()")
# [EOF]


#invoke some function:
#!











#part 2: (invoking func)
# /home/cisco/PycharmProjects/training/venv/bin/python /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py
# > <string>(1)<module>()
# (Pdb) s
# --Call--
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py(3)pdb_jump()
# -> def pdb_jump():
# (Pdb) b 8
# Breakpoint 1 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:8
# (Pdb) b 5
# Breakpoint 2 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:5
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:8
# 2   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py:5
# (Pdb) pdb.run("pdb_jump()")
# Entered into pdb jump func
# Looping through the list..
# 1
# 2
# 3
# 4
# 5
# (Pdb) l
#   1  	import pdb
#   2
#   3  ->	def pdb_jump():
#   4  	    print ("Entered into pdb jump func")
#   5 B	    l1 = [1,2,3,4,5]
#   6  	    print ("Looping through the list..")
#   7  	    for var in l1:
#   8 B	        print (var)
#   9  	pdb.run("pdb_jump()")
#  10
#  11  	# /home/cisco/PycharmProjects/training/venv/bin/python /home/cisco/PycharmProjects/training/day_nine/pdb_exec_jump.py
# (Pdb) c
# Entered into pdb jump func
# Looping through the list..
# 1
# 2
# 3
# 4
# 5
#
# Process finished with exit code 0