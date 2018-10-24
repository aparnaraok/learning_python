class Test(object):
    def __getitem__(self, items):
        print ('%-15s  %s' % (type(items), items))

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]


class Test(object):
    def __call__(self, *args, **kwargs):
        print (args)
        print (kwargs)
        print ('-'*80)

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)