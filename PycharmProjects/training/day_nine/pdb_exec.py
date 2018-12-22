import pdb

def f1(some_arg):
    some_other = some_arg + 1
    print (some_other)
    myadd(some_arg, some_other)
    return f2(some_other)

def f2(some_arg):
    some_other = some_arg + 1
    some_other = 2 * some_other - 17
    some_arg = 3 * (some_other + 12)
    myadd(some_arg, some_other)
    some_other = some_other + some_arg
    print (some_other)
    return f3(some_other)

def f3(some_arg):
    some_other = some_arg + 1
    print (some_other)
    return f4(some_other)

def f4(some_arg):
    some_other = some_arg + 1
    some_other = 2 * some_other - 17
    some_arg = 3 * (some_other + 12)
    some_other = myarith(some_other, some_arg)
    print (some_other)
    return some_other

def myadd(x, y):
    print ("x is ", x)
    print (x + y)
def myarith(x ,y):
    x  = 9/x + 1.8*y
    y = 7.8*(x/9 + 2.3*y)
    return x + y

pdb.run("f1(1)")

#debugger commands  :
#s single stepping
#--> repr about to exec line
#p some_arg (p means print)

#n will not step into a func whereas s will step into the func.
#@print always use n


# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(7)f1()
# -> return f2(some_other)
# (Pdb) s
# --Call--
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(9)f2()
# -> def f2(some_arg):
# (Pdb) s
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(10)f2()
# -> some_other = some_arg + 1
# (Pdb) s
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(11)f2()
# -> some_other = 2 * some_other - 17
# (Pdb) s
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(12)f2()
# -> some_arg = 3 * (some_other + 12)
# (Pdb) s
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(13)f2()
# -> myadd(some_arg, some_other)
# (Pdb) s
# --Call--
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(31)myadd()
# -> def myadd(x, y):
# (Pdb) n
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(32)myadd()
# -> print ("x is ", x)
# (Pdb) n
# x is  3
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(33)myadd()
# -> print (x + y)
# (Pdb) n
# -8
# --Return--
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(33)myadd()->None
# -> print (x + y)
# (Pdb) n
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(14)f2()
# -> some_other = some_other + some_arg
# (Pdb) c
# -8
# -7
# -1086.8793103448274



#####################BREAK POINTS>>>>>>>>>>>>...

#b f2(breakpoint to a func)
#b 19(brkpoint to a line ..ensure tat the line is not empty)
#b 29

#list all brkpoints:
#b



#c >>>>contiue till the 1st brkpoint
#s or n

#!some_other = -0.913


#
# /home/cisco/PycharmProjects/training/venv/bin/python /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py
# > <string>(1)<module>()
# (Pdb) s
# --Call--
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(3)f1()
# -> def f1(some_arg):
# (Pdb) b f2
# Breakpoint 1 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:9
# (Pdb) b 15
# Breakpoint 2 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# (Pdb) b 27
# Breakpoint 3 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:27
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:9
# 2   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# 3   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:27
# (Pdb) c
# 2
# x is  1
# 3
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(10)f2()
# -> some_other = some_arg + 1
# (Pdb) l
#   5  	    print (some_other)
#   6  	    myadd(some_arg, some_other)
#   7  	    return f2(some_other)
#   8
#   9 B	def f2(some_arg):
#  10  ->	    some_other = some_arg + 1
#  11  	    some_other = 2 * some_other - 17
#  12  	    some_arg = 3 * (some_other + 12)
#  13  	    myadd(some_arg, some_other)
#  14  	    some_other = some_other + some_arg
#  15 B	    print (some_other)
# (Pdb) disable 2
# Disabled breakpoint 2 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:9
# 	breakpoint already hit 1 time
# 2   breakpoint   keep no    at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# 3   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:27
# (Pdb) c
# x is  3
# -8
# -8
# -7
# > /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py(27)f4()
# -> some_other = myarith(some_other, some_arg)
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:9
# 	breakpoint already hit 1 time
# 2   breakpoint   keep no    at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# 3   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:27
# 	breakpoint already hit 1 time
# (Pdb) enable 2
# Enabled breakpoint 2 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:9
# 	breakpoint already hit 1 time
# 2   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# 3   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:27
# 	breakpoint already hit 1 time
# (Pdb) disable 2
# Disabled breakpoint 2 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:9
# 	breakpoint already hit 1 time
# 2   breakpoint   keep no    at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# 3   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:27
# 	breakpoint already hit 1 time
# (Pdb) del 2
# *** SyntaxError: can't delete literal
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
# (Pdb) clear 2
# Deleted breakpoint 2 at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:15
# (Pdb) b
# Num Type         Disp Enb   Where
# 1   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:9
# 	breakpoint already hit 1 time
# 3   breakpoint   keep yes   at /home/cisco/PycharmProjects/training/day_nine/pdb_exec.py:27
# 	breakpoint already hit 1 time
# (Pdb) c
# -1086.8793103448274

##########################temporary break point############
#tbreak

#c ....it will get deleted (prev one)
#j jump around...reexecute the code

#with new val

#j is within the function
#can jump up/below

#jumping ahead/back/illegal jumps
#can't jump into the middle of the block in for loop
#code in the finally block need to be executed so you can't jump out of the block.

#invoke some function:
#!pdb.run("<func_name(args)>")
#!pdb.run("f4(9)")
#cursor will remain as it is