import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print ("Cannot open file : : ", arg)
    else:
        print (arg, "has", len(f.readlines()), 'lines')
        f.close()