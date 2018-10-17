import sys
try:
    f = open('myfile.txt')
    val = int(f.readline().strip())
    f.close()
except FileNotFoundError:
    print ("No such file")
except ValueError:
    print ("Not a num")
except:
    print ("Unexpected error>>>>", sys.exc_info()[0])
    raise