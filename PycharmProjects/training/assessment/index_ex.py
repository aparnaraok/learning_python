a = [1,2,3,4,5,6]

for i in a:
    if (i%2 == 0) and a.index(i)%2 != 0:
        for j in a:
            if a.index(j)%2 == 0 and j%2 != 0:
                temp = j
                j=i
                i=temp
                a[a.index(j)] = i
                a[a.index(i)] = j
print(a)


import datetime
import time

def get_random(end):
    l = []
    end = end +1
    #for i in range(0,10):
    d = int(datetime.datetime.now().microsecond)
    print(d)
    d = d%end
        #l.append(d[-2:])

    return d



def get_random1(start, end):
    l = []
    #for i in range(0,10):
    d = get_random(end - start)
    d = d + start
    #l.append(d[-2:])
    l.append(d)
    return l

print(get_random1(10,12))


keys = []
values = []
def get_key(dic):
    print(dic)
    if type(dic.keys()) is dict:
    #dic = {'a' : {'b' : {'c' : {'d' : {'e'}}}}}
        #print(dic)
        keys.append(get_key(dic.keys()))
    else:
        values.append(dic.values())


dic = {'a' : {'b' : {'c' : {'d' : {'e'}}}}}
get_key(dic)
print(keys, values)