def file_wr(filename):
    f = open(filename, 'w')
    f.write('aaaaaaaa\n')
    f.write('bbbbbbbb\n')
    f.write('ccccccccc\n')
    f.close()

def file_rd(filename):
    f = open(filename)
    #print (f.read()) #prints string present in the file
    print (f.readline())
    print (f.readline())
    print(f.seek(9,0))
    print (f.tell())
    print (f.readlines())
    f.close()

def list_wr(filename, lst):
    f = open(filename, 'w')
    lst = list(map(lambda x : str(x) + '\n', lst))

    f.writelines(lst)
    f.close()
def list_rd(filename):
    f = open(filename, 'r')
    read_list = f.readlines()
    print ("Read list>>>", read_list)

    print(list(map(lambda x : x.strip(), read_list)))
    print (list(map(lambda x : int(x), read_list)))
    print (type(read_list[0]))

def dict_wr(filename, d1):
    f = open(filename, 'w')
    for (k, v) in d1.items():
        f.write(str(k)  + "," + str(v) + '\n')
    f.close()

def dict_rd(filename):
    f = open(filename)
    content = list(map(lambda x : x.strip(), f.readlines()))
    content =list(map(lambda x : x.split(','), content))
    content = dict(map(lambda x : (x[0], int(x[1])), content))
    print ("Content>>>.", content)

grades = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}



lst1 = [1,2,3,4]
if __name__ == '__main__':
    #file_wr('output.txt')
    #file_rd('output.txt')
    #print ("output file created successfully....")
    #list_rd('listout.txt')
    print ("file read sucessfully")
    #list_wr('listout.txt', lst1)
    #dict_wr('output_file.csv', grades)
    #print ("dict written succesfully")
    dict_rd('output_file.csv')