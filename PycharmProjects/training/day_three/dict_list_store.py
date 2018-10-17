import numpy as np
from numpy import *
def store_dict():
    mydict = {'pnq' : [12,11,15],
              'mac' : [43,76,89]}
    f = open('dump_data.csv', 'w')
    f.write(','.join(mydict.keys()) + '\n')
    i = 0

    while i < len(mydict['pnq']):
        f.write(str(mydict['pnq'][i]) + ',' +
                str(mydict['mac'][i]) + '\n')
        i = i + 1
    f.close()

def dict_rd(filename):
    f = open(filename)
    content = list(map(lambda x : x.strip(), f.readlines()))
    content =list(map(lambda x : x.split(','), content))
    #content = dict(map(lambda x : (x[0], int(x[1])), content))
    print ("Content>>>.", content)

    content_arr = np.array(content[1:])
    print (content_arr)

    content_list = list(content_arr.T)
    print (content_list)

    data = dict(zip(content[0], content_list))
    print(data)

if __name__ == '__main__':
    #store_dict()
    print ("Data entered successfully into the CSV file")
    dict_rd('dump_data.csv')