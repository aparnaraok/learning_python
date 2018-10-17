###Default arguments  and Keyword arguments.......(Especially used in  Notepad launching applications)
from functools import  reduce

def login(name, paswd= 'some_pass', host = 'asterix'):
    print ("Username is ", name)
    print ("Password is ", paswd)
    print ("Hostname is ", host)

if __name__ == '__main__':
    login('abcd', host = 12)



def func(a, b, c):
    return a + b - c
print (func(2, 1, 4))
print(func(2, c = 5, b = 10))
print(func(c=4, b=6, a = 4))
#print(func(c=4, b=6, 4))


def varargs(*args):
    print ("Arguments inside>>>>>", args)
if __name__ == '__main__':
    varargs('s','d')
    varargs(12,10,98)

def varkwargs(*args, **kwargs):
    print ("Non Kw Arguments inside>>>>>", args)
    print ("Keyword arguments>>>", kwargs)
if __name__ == '__main__':
    print ("With non keywords")
    varkwargs('s','d')
    print ("With only keywords")
    varkwargs(x='a', y='b')
    print ("With both kw and now nw args")
    varkwargs('a','b',u=1,v=2,w=3)





def square(x):
    print ("Square is >>>>>", x * x)
    return x * x
def double(x):
    print ("Double is >>>>", 2 * x)
    return 2 * x
def applier(q, x):
    return q(x)
applier(square, 8)
applier(double, 7)


'''
def applier2(q, x, y):
    #print ("Type is ", type(q))
    #if type(q) is function:
    return q(x, y)
def myadd(x, y):
    return x + y
print (applier2(myadd, 4, 5))

print (dir(applier2))
def applier3(q, x):
    return q(x)
print (applier3(lambda x : x * x, 5)

'''
def myfunc(n):
    return lambda  x : n + x
f1 = myfunc(5)
f2 = myfunc(10)
print (f1(6))
ie = myfunc("http://")
cr = myfunc("https://")
print (ie("google.com"))

def square(x):
    return x * x
def even(x):
    return x % 2 == 0

print ((map(square, range(10,20))))
print (type((filter(even, range(10,20)))))


print (list(map(square, range(10,20))))
print (list(filter(even, range(10,20))))

li1 = ['a.in', 'b.in', 'c.in']
print (list(map(lambda x : 'https://' + x, li1)))

sem1 = [1,2,3,4,5,6,7,8]
sem2 = [6,7,8,9,10]

print (list(map(lambda x, y : x + y, sem1, sem2)))

print (reduce(lambda x, y : x + y, sem1))


url = "http://www.google.com"
urllist = list(url)
print ("Urllist>>>>>", urllist)

urllist.insert(4, 's')
print ("After insrting>>>>>", urllist)

print (reduce(lambda x,y : x +y , urllist))

print (list(zip(sem1, sem2)))
print (dict(zip(sem1, sem2)))